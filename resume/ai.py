import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_resume(text):

    prompt = f"""
You are an ATS Resume Analyzer.

Analyze this resume and return:

1. Name
2. Skills
3. Education
4. Experience
5. Projects
6. Certifications
7. ATS Score out of 100
8. Professional Summary

Resume:

{text}
"""

    response = model.generate_content(prompt)

    return response.text