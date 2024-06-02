"""
This module contains the main configurations for FastAPI to run.
"""
 
from fastapi import FastAPI
from route.api import router
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
 
PREFIX_V1 = "/challenge_1"
 
TAGS_METADATA = [
    {
        "name": "challenge1",
        "description": "upload image, create mask image and display both original & mask image"
    }
]
 
app = FastAPI(
    title="Challenge1 Application",
    openapi_tags=TAGS_METADATA,
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
)
 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)
 
app.include_router(router, prefix=PREFIX_V1)
 
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=7000,
        reload=False
    )