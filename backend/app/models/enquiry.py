from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import JSON
from sqlalchemy import DateTime
from sqlalchemy.sql import func

from app.db.database import Base


class Enquiry(Base):
    __tablename__ = "enquiries"

    id = Column(Integer, primary_key=True)

    name = Column(String)

    email = Column(String)

    phone = Column(String)

    message = Column(Text)

    status = Column(
        String,
        default="NEW"
    )

    ai_extraction = Column(JSON)

    ai_reply = Column(Text)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )