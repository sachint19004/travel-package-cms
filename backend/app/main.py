from fastapi import FastAPI

app = FastAPI(
    title="Travel Package CMS API"
)

@app.get("/")
def root():
    return {
        "status": "healthy",
        "service": "travel-package-cms"
    }
    