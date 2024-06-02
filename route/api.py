"""
 
Routes:
    - GET /health : Performs a health check and returns a HealthCheckResponse.
"""
from fastapi import APIRouter
import challenge1
from model.model import HealthCheckResponse,Status
router = APIRouter()
 
 
@router.get(
    "/health",
    status_code=200,
    tags=["Health check"],
)
async def health_check():
    """
    Performs a health check and returns a HealthCheckResponse.
 
    Returns:
        HealthCheckResponse: The health check response.
    """
    return HealthCheckResponse(status=Status.success,message="Healthy")
 
 
router.include_router(challenge1.router)
    