import json

import google.generativeai as genai

from app.core.config import settings


def extract_enquiry_details(message: str):

    genai.configure(
        api_key=settings.GEMINI_API_KEY
    )

    model = genai.GenerativeModel(
        "gemini-3.6-flash"
    )

    prompt = f"""
Extract the following:

- adults
- children
- destination
- nights
- budget
- month
- must_have
- confidence

Return ONLY a valid JSON object.

Do not use markdown.
Do not use code blocks.
Do not add explanations.

Message:
{message}
"""

    response = model.generate_content(
        prompt
    )

    cleaned_text = (
        response.text
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    return json.loads(cleaned_text)