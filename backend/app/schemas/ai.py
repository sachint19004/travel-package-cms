from pydantic import BaseModel


class EnquiryExtractionRequest(BaseModel):
    message: str