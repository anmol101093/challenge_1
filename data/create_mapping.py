import json
import pandas as pd
import os
"""
create mapping for image and annotations bases on input annotation json file

"""
annotation_file_path=os.path.join(os.getcwd(),'input','coin-dataset','_annotations.coco.json')

with open(annotation_file_path,'r') as file:
    data=json.load(file)

images=data['images']
images_df=pd.DataFrame(data=images)

images_df.to_csv('data/mapping/images.csv',index=None)

annotations=data['annotations']
annot_df=pd.DataFrame(data=annotations)

annot_df.to_csv('data/mapping/annotations.csv',index=None)