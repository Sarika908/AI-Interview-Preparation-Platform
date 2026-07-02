import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_interview_question(category):
    prompt = f"""
You are an expert technical interviewer.

Generate ONE {category} interview question.

Return only the question.
"""

    response = model.generate_content(prompt)
    return response.text


def evaluate_answer(question, answer):
    prompt = f"""
You are a senior software engineer interviewer.

Question:
{question}

Candidate Answer:
{answer}

Evaluate the answer.

Return in this format:

Score: X/10

Strengths:
...

Weaknesses:
...

Correct Answer:
...

Improvement Tips:
...
"""

    response = model.generate_content(prompt)
    return response.text