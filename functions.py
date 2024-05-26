import os
import uuid
import json
import PyPDF2
import numpy as np
import openai
from openai import OpenAI
from app import get_api_key


def learn_pdf(file_path):
    content_chunks = []
    pdf_file = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    for page in pdf_reader.pages:
        content = page.extract_text()
        obj = {
            "id": str(uuid.uuid4()),
            "text": content,
            "embedding": None  # Placeholder, replace with actual embedding
        }
        content_chunks.append(obj)

    json_file_path = 'my_knowledgebase.json'
    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for i in content_chunks:
        data.append(i)
    with open(json_file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    pdf_file.close()

def Answer_from_documents(user_query, api_key):
    openai.api_key = api_key

    user_query_vector = None  # Placeholder, replace with actual vector

    openai = OpenAI()

    with open('my_knowledgebase.json', 'r', encoding="utf-8") as jsonfile:
        data = json.load(jsonfile)
        for item in data:
            item['embeddings'] = None  

        for item in data:
            item['similarities'] = None  
        sorted_data = sorted(data, key=lambda x: x['similarities'], reverse=True)

        context = ''
        for item in sorted_data[:2]:
            context += item['text']

        messages = [
            {"role": "user", "content": f"The following is a Context:\n{context}\n\n Answer the following user query according to the above given context.\n\nquery: {user_query}"}
        ]

        completion = openai.chat.completions.create(messages=messages, model="gpt-3.5-turbo")

    return completion['choices'][0]['message']['content']


def save_uploaded_file(uploaded_file):
    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())
