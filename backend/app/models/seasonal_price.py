from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import Date
from sqlalchemy import Numeric

from app.db.database import Base


class SeasonalPrice(Base):
    __tablename__ = "seasonal_prices"

    id = Column(Integer, primary_key=True)

    package_id = Column(
        Integer,
        ForeignKey("packages.id")
    )

    season = Column(String)

    price_per_person = Column(
        Numeric(10, 2)
    )

    gst_percent = Column(
        Numeric(5, 2)
    )

    sharing_basis = Column(String)

    start_date = Column(Date)

    end_date = Column(Date)