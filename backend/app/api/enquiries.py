from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.database import get_db

from app.models.enquiry import Enquiry

from app.schemas.enquiry import (
    EnquiryCreate
)

router = APIRouter(
    prefix="/enquiries",
    tags=["Enquiries"]
)

@router.post("/")
def create_enquiry(
    enquiry: EnquiryCreate,
    db: Session = Depends(get_db)
):
    new_enquiry = Enquiry(
        name=enquiry.name,
        email=enquiry.email,
        phone=enquiry.phone,
        message=enquiry.message
    )

    db.add(new_enquiry)

    db.commit()

    db.refresh(new_enquiry)

    return new_enquiry

@router.get("/")
def get_enquiries(
    db: Session = Depends(get_db)
):
    return (
        db.query(Enquiry)
        .order_by(
            Enquiry.created_at.desc()
        )
        .all()
    )

@router.get("/{enquiry_id}")
def get_enquiry(
    enquiry_id: int,
    db: Session = Depends(get_db)
):
    return (
        db.query(Enquiry)
        .filter(
            Enquiry.id == enquiry_id
        )
        .first()
    )