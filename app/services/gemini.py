import os
import google.generativeai as genai
from app.core.prompts import yt_content_prompt

genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

gemini_pro_model = genai.GenerativeModel("gemini-1.0-pro")

def generate_text(prompt: str):
    model_response = gemini_pro_model.generate_content(prompt)
    return model_response.text