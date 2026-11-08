from pydantic import BaseModel


class EnquiryExtractionRequest(BaseModel):
    message: str

class PackageSuggestionRequest(BaseModel):
    message: str