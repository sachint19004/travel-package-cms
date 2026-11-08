from fastapi import APIRouter

from app.schemas.ai import (
    EnquiryExtractionRequest
)

from app.services.ai_service import (
    extract_enquiry_details
)

router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)


@router.post("/extract")
def extract_enquiry(
    payload: EnquiryExtractionRequest
):
    return extract_enquiry_details(
        payload.message
    )