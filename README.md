# PDF SCAN

PDF SCAN is a simple application that allows users to upload PDF files, extract text content from them, and then query that content using OpenAI's GPT-3.5 model.

## Project Setup

To set up the project, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Make sure you have an OpenAI API key.
4. Run `python app.py` to start the application.

## Functionalities

1. **Upload PDF:** Users can upload a PDF file using the file uploader interface.
2. **Read PDF:** After uploading a PDF, users can click the "Read PDF" button to extract text content from the uploaded PDF file.
3. **Ask Question:** Users can input a query in the text input field and click the "Send" button to get an answer based on the extracted content from the PDF.

## Usage Instructions

1. Upon running the application, you will see a title "PDF SCAN" along with a file uploader.
2. Click on the file uploader and select the PDF file you want to extract text from.
3. After uploading the file, click the "Read PDF" button to initiate the text extraction process.
4. Once the extraction is complete, you can input your query in the text input field labeled "Enter your Query."
5. Click the "Send" button to get the response from the model based on the extracted text and your query.
