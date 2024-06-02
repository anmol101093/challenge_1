"""
This module contains pydantic validation models.
"""
from enum import Enum
from pydantic import BaseModel
 
 
class Status(str, Enum):
    failure = "failure"
    success = "success"
 
 
class HealthCheckResponse(BaseModel):
    status: Status
    message: str
 
 
class ListObjectModel(BaseModel):
    image_name: str

class getObjectDetailsModel(BaseModel):
    object_id: int