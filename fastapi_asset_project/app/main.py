from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from app.api.api import api_router
from app.db.database import engine
from app.models.asset import Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Asset API",
    description="FastAPI version of the Asset API for performance comparison with Django",
    version="0.1.0",
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API router
app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
