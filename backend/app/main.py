from fastapi import FastAPI

from app.api.auth import router as auth_router
from app.api.packages import router as package_router
from app.api.pricing import router as pricing_router
from app.api.ai import router as ai_router
from app.api.enquiries import router as enquiry_router

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Travel Package CMS API"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(package_router)
app.include_router(pricing_router)
app.include_router(enquiry_router)
app.include_router(ai_router)

@app.get("/")
def health_check():
    return {
        "status": "healthy",
        "service": "travel-package-cms"
    }