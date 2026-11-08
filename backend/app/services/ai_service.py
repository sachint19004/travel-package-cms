import json
import importlib
import google.generativeai as genai
import json
import re
from app.core.config import settings


def extract_enquiry_details(message: str):

    try:
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

    except Exception as e:

        print(
            f"Gemini failed: {e}"
        )

        return extract_with_ollama(
            message
        )


def extract_with_ollama(message: str):

    ollama = importlib.import_module("ollama")

    prompt = f"""
Extract:

adults
children
destination
nights
budget
month
must_have
confidence

Return ONLY valid JSON.

Message:
{message}
"""

    response = ollama.chat(
        model=settings.OLLAMA_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    import json

    print(
    response["message"]["content"]
)

    content = response["message"]["content"]

    match = re.search(
        r"\{.*\}",
        content,
        re.DOTALL
    )

    if not match:
        return {
            "error": "No JSON found",
            "raw_response": content
        }

    return json.loads(match.group())