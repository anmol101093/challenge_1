
from config import Paths
import pandas as pd
import math
import ast
from src.backend.errors import ImageReferenceNotFoundError,IDReferenceNotFoundError

def fetchobjects(image_name):

    '''
    Accept Paramter: Image Name 
    response : return the details of each circular objects present in the input image
               its ID's and its BBOX.  
    '''

    image_data=pd.read_csv(Paths.image)
    annot_data=pd.read_csv(Paths.annotations)
    try:
        image_id=image_data[image_data['file_name']==image_name]['id'].to_list()[0]
        object_dict={
        'image_name':image_name,
        'image_id':image_id,
        'id':[],
        'bbox':[]
         }
        filter_df=annot_data[annot_data['image_id']==image_id]
        filter_df=filter_df.sort_values(by='id')
            
        for _, row in filter_df.iterrows():
            object_dict['id'].append(row['id'])
            object_dict['bbox'].append(row['bbox'])

        return object_dict
    
    except:
        raise ImageReferenceNotFoundError(description=f"Reference for image - {image_name} not found in the database")

def getDetails(id):

    '''
    Accept Paramter: Circular Object ID 
    response : return the bbox, radius & centroid details of input Object ID.  
    '''

    annot_data=pd.read_csv(Paths.annotations)
    #filter object based on it's unique id
    filter_df=annot_data[annot_data['id']==id]

    result={}
    
    if len(filter_df)>0:
        result['bbox']=filter_df['bbox'].to_list()[0]

        # as this approach is widely accepted x,y, width, height so i have not chosen the other combination x,y,height & width
        
        
        x,y,width,height=ast.literal_eval(result['bbox'])
        if width==height:
            result['radius']=math.sqrt(filter_df['area'].to_list()[0])/2
        else:
            result['radius']=min(width,height)/2
            
        centroid_x=x+(width/2)
        centroid_y=(y+height/2)

        result['centroid']=(centroid_x,centroid_y)

        return result
    
    else:
        raise IDReferenceNotFoundError(description=f"Circular Object Id Reference - {id} not found in the database")




