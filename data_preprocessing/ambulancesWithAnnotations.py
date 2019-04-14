#extract ambulance images that have annotations

import os
from shutil import copy

#images are .jpg
fireTruck_imgs_path = "/Users/Stevengrosz/Documents/X_491/fireTruckData/images"
#annotations are .xml files
fireTruck_annotations_path = "/Users/Stevengrosz/Documents/X_491/fireTruckData/Annotation/n03345487"
#output folders for subset of ambulance data we want
imgs_output_path = "/Users/Stevengrosz/Documents/X_491/fireTruckDataSub/images"
annotations_output_path = "/Users/Stevengrosz/Documents/X_491/fireTruckDataSub/Annotations"

fireTruck_annotations = [os.path.join(fireTruck_annotations_path,fname) for fname in
              os.listdir(fireTruck_annotations_path) if fname.endswith('.xml')]

count = 0

for annotation_file in fireTruck_annotations:
    annotation_split = annotation_file.split('/')
    annotation_fileID = annotation_split[8]
    annotation_fileID = annotation_fileID[0:-4]

    imgs_file_path = fireTruck_imgs_path + "/" + str(annotation_fileID) + ".jpeg"
    annotations_file_path = str(annotation_file)

    #copy each image that has an annoation associated
    exists = os.path.isfile(imgs_file_path)
    if exists:
        count = count + 1
        copy(imgs_file_path, imgs_output_path)
        copy(annotations_file_path, annotations_output_path)
    else:
        continue

print("num of fireTruck imgs: ")
print(count)
