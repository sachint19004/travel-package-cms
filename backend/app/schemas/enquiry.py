from pydantic import BaseModel
from pydantic import EmailStr


class EnquiryCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    message: str