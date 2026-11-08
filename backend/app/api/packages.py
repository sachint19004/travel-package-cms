from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.db.database import get_db

from app.models.package import Package
from app.models.package_version import PackageVersion
from app.schemas.package import (
    PackageCreate,
    PackageResponse
)

router = APIRouter(
    prefix="/packages",
    tags=["Packages"]
)

@router.post(
    "/",
    response_model=PackageResponse
)
def create_package(
    package: PackageCreate,
    db: Session = Depends(get_db)
):
    new_package = Package(
        package_code=package.package_code,
        slug=package.slug,
        title=package.title,
        description=package.description,
        days=package.days,
        nights=package.nights,
        hotels=package.hotels,
        inclusions=package.inclusions,
        itinerary=package.itinerary,
        cover_image=package.cover_image
    )

    db.add(new_package)

    db.commit()

    db.refresh(new_package)

    return new_package@router.get(
    "/",
    response_model=list[PackageResponse]
)
def get_packages(
    db: Session = Depends(get_db)
):
    return db.query(Package).all()

@router.get(
    "/{package_id}",
    response_model=PackageResponse
)
def get_package(
    package_id: int,
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

    return package

@router.put("/{package_id}")
def update_package(
    package_id: int,
    payload: PackageCreate,
    db: Session = Depends(get_db)
):
    package = (
        db.query(Package)
        .filter(Package.id == package_id)
        .first()
    )

    if not package:
        raise HTTPException(
            status_code=404,
            detail="Package not found"
        )

    version_count = (
        db.query(PackageVersion)
        .filter(
            PackageVersion.package_id == package.id
        )
        .count()
    )

    package_version = PackageVersion(
        package_id=package.id,
        version_number=version_count + 1,
        snapshot={
            "package_code": package.package_code,
            "slug": package.slug,
            "title": package.title,
            "description": package.description,
            "days": package.days,
            "nights": package.nights,
            "hotels": package.hotels,
            "inclusions": package.inclusions,
            "itinerary": package.itinerary,
        }
    )

    db.add(package_version)

    package.package_code = payload.package_code
    package.slug = payload.slug
    package.title = payload.title
    package.description = payload.description
    package.days = payload.days
    package.nights = payload.nights
    package.hotels = payload.hotels
    package.inclusions = payload.inclusions
    package.itinerary = payload.itinerary
    package.cover_image = payload.cover_image

    db.commit()

    db.refresh(package)

    return package

@router.delete("/{package_id}")
def delete_package(
    package_id: int,
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

    db.delete(package)

    db.commit()

    return {
        "message": "Package deleted successfully"
    }

@router.get("/{package_id}/versions")
def get_package_versions(
    package_id: int,
    db: Session = Depends(get_db)
):
    versions = (
        db.query(PackageVersion)
        .filter(
            PackageVersion.package_id == package_id
        )
        .all()
    )

    return versions