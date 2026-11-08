from pydantic import BaseModel
from app.models.package_version import PackageVersion

class PackageCreate(BaseModel):
    package_code: str
    slug: str
    title: str
    description: str
    days: int
    nights: int
    hotels: str
    inclusions: str
    itinerary: list
    cover_image: str | None = None

class PackageResponse(PackageCreate):
    id: int

    class Config:
        from_attributes = True

