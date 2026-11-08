from pydantic import BaseModel


class SeasonalPriceCreate(BaseModel):
    season: str
    price_per_person: float
    gst_percent: float
    sharing_basis: str