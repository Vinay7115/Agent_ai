import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))
API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini model
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

def call_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Error: {str(e)}"
