from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.db.database import get_db

from app.models.package import Package

from app.schemas.ai import (
    EnquiryExtractionRequest,
    PackageSuggestionRequest
)

from app.services.ai_service import (
    extract_enquiry_details
)

from app.services.package_matcher import (
    get_best_packages
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

@router.post("/suggest")
def suggest_packages(
    payload: PackageSuggestionRequest,
    db: Session = Depends(get_db)
):

    extraction = extract_enquiry_details(
        payload.message
    )

    packages = (
        db.query(Package)
        .all()
    )

    suggestions = get_best_packages(
        packages,
        extraction
    )

    return {
        "extraction": extraction,
        "suggestions": suggestions
    }