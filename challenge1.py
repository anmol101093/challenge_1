"""
This module contains Fast API routes for handling search image based on depth min & max.
 
Routes:
    - POST /search_images : extracting images from database for min & max depth.
"""
 
import matplotlib.pyplot as plt
from model.model import Status,ListObjectModel, getObjectDetailsModel
from src.backend.coinObjects import fetchobjects, getDetails
from src.backend.mask import getmaskImage
from minio import Minio
from minio.error import S3Error
import io
from fastapi import File, UploadFile, HTTPException,APIRouter
from fastapi.responses import StreamingResponse
from src.backend.errors import IDReferenceNotFoundError,ImageReferenceNotFoundError
import os

minio_client = Minio(
endpoint="minio:9000",
    access_key="root",
    secret_key="password",
    secure=False
)

router = APIRouter()
 
@router.post(
        "/upload",
        status_code=200,
        description="read the file steams and upload it to mini-io S3 Bucket for persistent storage"
        )
async def upload(file: UploadFile = File(...)):

    # create bucket in minio if not exists
    try:
        bucket_name = "temp-bucket"
        if not minio_client.bucket_exists(bucket_name):
            minio_client.make_bucket(bucket_name)
    except S3Error as err:
        raise HTTPException(status_code=500, detail=f"Error creating bucket: {err}")
    
    # Read file content
    try:
        contents = await file.read()
        file_content = io.BytesIO(contents)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading file: {str(e)}")
 
    # Upload file to MinIO
    try:
        file_name = file.filename
        file_length = len(contents)
        minio_client.put_object(
            bucket_name=bucket_name,
            object_name=file_name,
            data=file_content,
            length=file_length,
            content_type=file.content_type
        )
    except S3Error as err:
        raise HTTPException(status_code=500, detail=f"Error uploading file: {err}")
    
    return {"message": f"Successfully uploaded {file.filename} to bucket {bucket_name}"}
 

@router.get(
    "/list_objects",
    status_code=200,
    description="returns the id and bounding boxes for each circular objects for an image"
)
async def listObjects(params:ListObjectModel):
    image_name=params.image_name
    try:
        object_list=fetchobjects(image_name)
        return {"status": Status.success, "response": object_list}
    
    except ImageReferenceNotFoundError as e:
        return {"status":Status.failure,
            "message": e.description
        }
    

@router.get(
    "/get_object_details",
    status_code=200,
    description="returns the bounding box, radius & centroid for queried circular object"
)
async def listObjects(params:getObjectDetailsModel):
    object_id=params.object_id
    try:
        result=getDetails(object_id)
        return {"status": Status.success, "response": result}
    
    except IDReferenceNotFoundError as e:
        return {"status":Status.failure,
            "message": e.description
        }


@router.get(
    "/mask_image",
    status_code=200,
    description="mask the circular object and return original and masked image"
)
async def maskImage(params:ListObjectModel):
    bucket_name = "temp-bucket"
    if not minio_client.bucket_exists(bucket_name):
        raise HTTPException(status_code=500, detail=f"S3 bucket does not exist, try /upload api to create \
                            and upload a file")
    
    image_name=params.image_name
    
    file_path=os.path.join(os.getcwd(),'data','minio-data',image_name)
    
    # Download file from MinIO bucket
    try:
        minio_client.fget_object(bucket_name, image_name, file_path)
    except S3Error as err:
        msg=f"image -{image_name} not found in minio bucket, please upload it first using /upload api"
        return {"status": Status.failure,"message": msg,"response": err}
    
    try:
    
        original_image, masked_image=getmaskImage(image_name,file_path)

        _, (ax1,ax2)= plt.subplots(1,2,figsize=(5,15))
        ax1.imshow(original_image)
        ax1.set_title("original Image")

        ax2.imshow(masked_image)
        ax2.set_title("masked Image")

        plt.tight_layout()

        # Save plot to a BytesIO object
        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        plt.close()

        return StreamingResponse(buf, media_type="image/png")
    
    except IDReferenceNotFoundError as e:
        return {"status":Status.failure,
            "message": e.description
        }
    
    except ImageReferenceNotFoundError as e:
        return {"status":Status.failure,
            "message": e.description
        }