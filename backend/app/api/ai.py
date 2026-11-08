from fastapi import APIRouter
import json

import google.generativeai as genai

from app.core.config import settings

from app.schemas.ai import (
    EnquiryExtractionRequest
)

router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)

@router.post("/extract")
def extract_enquiry(
    payload: EnquiryExtractionRequest
):

    genai.configure(
        api_key=settings.GEMINI_API_KEY
    )

    model = genai.GenerativeModel(
        "gemini-3.6-flash"
    )

    prompt = f"""
Extract the following from the enquiry.

Return ONLY valid JSON.

Fields:

adults
children
destination
nights
budget
month
must_have
confidence

Rules:
- budget should be a number only
- nights should be an integer
- confidence should be between 0 and 1

Message:
{payload.message}
"""

    response = model.generate_content(
        prompt
    )

    try:
        cleaned_text = (
    response.text
    .replace("```json", "")
    .replace("```", "")
    .strip()
)

        return json.loads(cleaned_text)

    except:
        return {
            "raw_response": response.text
        }

    