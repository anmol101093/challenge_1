**Challenge 1**

**Steps to execute the code.**

1. **Run docker-compose up -d 
    OR 
    pip install -e . and then Run main.py but we must change the API port in the postman collection which currently pointing to host port that is internally mapped to app container port ** 

2. **URL to check minio application up & running – [http://localhost:9000]**

   **username= root**

   **password= password**

**API Details** 

1. **/health**

       **Check Application Health.**

         <http://localhost:4000/challenge_1/health>

        **response** = {

    `"status": "success",

    "message": "Healthy"

      }


2. **/upload**

      **Select the image file to upload it to the Minio s3 bucket to persistently store it.**

     **Response**=

{

    "message": "Successfully uploaded 0ba4fa31-913c-45be-9e59-bc14fe4f324e_jpg.rf.89dddeb3544e94d2c5f1aa763b85823d.jpg to bucket temp-bucket"

}

3. **/list_objects**

    **Provide the name of the image file uploaded to the Bucket using " /upload " API.**

   **Body**= {
  "image_name": "4bc07dea-9e08-4802-99ae-fbcec55d410b_jpg.rf.fca64189ac38d4a1265341caf4d98e7f.jpg"
}

**Response**= 

{

    "status": "success",

    "response": {
        "image_name": "4bc07dea-9e08-4802-99ae-fbcec55d410b_jpg.rf.fca64189ac38d4a1265341caf4d98e7f.jpg",

        "image_id": 186,

        "id": [

            509,

            510,

            511,

           512,

            513

        ],

        "bbox": [

            "[410, 384, 204, 184]",

            "[616, 454, 205, 188]",

            "[236, 220, 197, 203]",

            "[404, 609, 212, 204]",

            "[170, 506, 213, 197]"

        ]

    }

}

4. **/get_object_details**

   **Provide the id to get the Bounding box, radius & centroid of a circular object**

   **Body**= {
    "object_id": 274
    }

**Response**= {

    "status": "success",

    "response": {

        "bbox": "[279, 115, 125, 123]",

       "radius": 61.5,

        "centroid": [

            341.5,

            176.5

        ]

    }

}






5. **/mask_image**

    **provide the name of the image that was uploaded & This API will output the original & masked Image** 

**Body**= 

{
  "image_name": "5b887c9d-79d6-4701-97b8-caccf7edd605_jpg.rf.1893fa59b5ab32d51b5857ed6dfd8da5.jpg"
}

**Response**= display original & masked image








