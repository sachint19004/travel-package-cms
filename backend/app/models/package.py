from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import JSON
from sqlalchemy import Text
from sqlalchemy.sql import func

from app.db.database import Base


class Package(Base):
    __tablename__ = "packages"

    id = Column(Integer, primary_key=True)

    package_code = Column(String, unique=True, nullable=False)

    slug = Column(String, unique=True, nullable=False)

    title = Column(String, nullable=False)

    description = Column(Text)

    days = Column(Integer)

    nights = Column(Integer)

    hotels = Column(String)

    inclusions = Column(Text)

    itinerary = Column(JSON)

    cover_image = Column(String)

    status = Column(String, default="DRAFT")

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )