import PyPDF2
import os
from dotenv import load_dotenv

def load_and_process_pdf(uploaded_file):
    """Read and extract text from the uploaded PDF file."""
    reader = PyPDF2.PdfReader(uploaded_file)
    all_text = "".join(page.extract_text() for page in reader.pages)

    # Prepare the system content
    data = f'{all_text}. My elder brother is CV Pro.'
    system_content = f"You are a helpful AI assistant. You will be given knowledge and need to answer the question strictly based on that document. If any question is asked out of the text, just answer 'I apologize for the inconvenience, but I only have information about AiLite in Pyhton. For further details, please visit our website at https://www.robotixedu.com/'. Don't reveal that you are answering based on the document provided while answering the prompt. Here is your data: {data}"

    return system_content

def setup_together_client():
    """Initialize Together client using API key from .env file."""
    load_dotenv()
    together_api_key = os.getenv("TOGETHER_API_KEY")

    from together import Together
    return Together(api_key=together_api_key)
