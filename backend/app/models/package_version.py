from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import JSON
from sqlalchemy import DateTime
from sqlalchemy.sql import func

from app.db.database import Base


class PackageVersion(Base):
    __tablename__ = "package_versions"

    id = Column(Integer, primary_key=True)

    package_id = Column(
        Integer,
        ForeignKey("packages.id")
    )

    version_number = Column(Integer)

    snapshot = Column(JSON)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
