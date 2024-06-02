import cv2
import numpy as np
from src.backend.coinObjects import fetchobjects, getDetails

def read_image(path):
    '''
    Accept Paramter: Path Image is stored 
    response : read the image and return it's pixels data in array format of shape (H,W,3). 
    '''
    image=cv2.imread(path)
    return image

def getmaskImage(image_name,image_path):
    '''
    Accept Paramter: Image Name , path where image is stored (image_path)
    response : return the original & masked image based on given centroid , radius for each 
               circular object.  
    '''
    image=read_image(image_path)
    object_id=get_ids(image_name)
    object_data=fetchdetails(object_id)

    # Create a mask of the same dimensions as the image (filled zeros)
    mask = np.zeros(image.shape[:2], dtype=np.uint8)
    for _, data in zip(object_id,object_data):
        centeroid = data["centroid"]
        radius = data["radius"]
        
        mask = cv2.circle(mask, centeroid, radius, 255, -1)
    
    # Apply the mask to the image
    masked_image = cv2.bitwise_and(image, image, mask=mask)

    return image, masked_image



def get_ids(image_name):
    
    object_data=fetchobjects(image_name)
    return object_data['id']

def fetchdetails(object_id):
    
    object_data = []
    for obj_id in object_id:
        data=getDetails(obj_id)
        temp={}
        if data:
            
            temp['radius']=int(data['radius'])    
            centroid=data['centroid']
            x,y=centroid
            temp['centroid']=[(int(x),int(y))][0]
            
            object_data.append(temp)
    
    return object_data