from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.db.database import get_db

from app.models.package import Package
from app.models.seasonal_price import SeasonalPrice

from app.schemas.pricing import (
    SeasonalPriceCreate
)

router = APIRouter(
    prefix="/pricing",
    tags=["Pricing"]
)

@router.post("/{package_id}")
def create_price(
    package_id: int,
    payload: SeasonalPriceCreate,
    db: Session = Depends(get_db)
):

    package = (
        db.query(Package)
        .filter(
            Package.id == package_id
        )
        .first()
    )

    if not package:
        raise HTTPException(
            status_code=404,
            detail="Package not found"
        )

    price = SeasonalPrice(
        package_id=package_id,
        season=payload.season,
        price_per_person=payload.price_per_person,
        gst_percent=payload.gst_percent,
        sharing_basis=payload.sharing_basis
    )

    db.add(price)

    db.commit()

    db.refresh(price)

    return price


@router.get("/{package_id}")
def get_prices(
    package_id: int,
    db: Session = Depends(get_db)
):
    return (
        db.query(SeasonalPrice)
        .filter(
            SeasonalPrice.package_id == package_id
        )
        .all()
    )
