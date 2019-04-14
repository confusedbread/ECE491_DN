#read voc data and extract only the images for person, bicycle, and car
#keep a count of how many images of each class we have
#save images to folder 491data/images/*.jpg
#save annotation files to folder 491data/Annotations/*.xml

import os
from shutil import copy

#label files are txt files
VOC2007_labels_path = "/Users/Stevengrosz/darknet/data/VOCdevkit/VOC2007/labels"
#images are .jpg
VOC2007_imgs_path = "/Users/Stevengrosz/darknet/data/VOCdevkit/VOC2007/JPEGImages"
#annotations are .xml files
VOC2007_annotations_path = "/Users/Stevengrosz/darknet/data/VOCdevkit/VOC2007/Annotations"
#output folders for subset of VOC data we want
labels_output_path = "/Users/Stevengrosz/darknet/data/491data/labels"
imgs_output_path = "/Users/Stevengrosz/darknet/data/491data/images"
annotations_output_path = "/Users/Stevengrosz/darknet/data/491data/Annotations"

VOC2007_labels = [os.path.join(VOC2007_labels_path,fname) for fname in
              os.listdir(VOC2007_labels_path) if fname.endswith('.txt')]
#VOC2007_imgs = [os.path.join(VOC2007_imgs_path,fname) for fname in
#              os.listdir(VOC2007_imgs_path) if fname.endswith('.jpg')]
#VOC2007_annotations = [os.path.join(VVOC2007_annotations_path,fname) for fname in
#              os.listdir(VOC2007_annotations_path) if fname.endswith('.xml')]

#labels_out = open(VOC2007_labels_path, 'w')
#imgs_out = open(VOC2007_imgs_path, 'w')
#annotations_out = open(VOC2007_annotations_path, 'w')

count_images = 0
count_bicycle = 0
count_person = 0
count_car = 0

for label_file in VOC2007_labels:
    copyFlag = 1;
    label_file_split = label_file.split('/')
    label_fileID = label_file_split[8]
    label_fileID = label_fileID[0:-4]

    #open each label.txt file and read class label
    #label_file_path = strcat(VOC2007_labels_path, "/", label_file)
    #imgs_file_path = strcat(VOC2007_imgs_path, "/", label_fileID, ".jpg")
    #annotations_file_path = strcat(VOC2007_annotations_path, "/", label_fileID, ".xml")

    label_file_path = str(label_file)
    imgs_file_path = VOC2007_imgs_path + "/" + str(label_fileID) + ".jpg"
    annotations_file_path = VOC2007_annotations_path + "/" + str(label_fileID) + ".xml"

    #if class is 1, 6, or 14 then save this label, image, and, annotation
    #1 = bicycle
    #6 = car
    #14 = person
    label_data = open(label_file_path, 'r')
    for line in label_data:
        line_split = line.split()
        class_label = line_split[0]
        if (class_label=="1" or class_label=="6" or class_label=="14"):
            print("correct class identified")
            if(class_label == "1"):
                temp_bicycle_count = temp_bicycle_count + 1
            elif(class_label == "6"):
                temp_car_count = temp_car_count + 1
            elif(class_label == "14"):
                temp_person_count = temp_person_count + 1
        else:
            copyFlag = 0;
    if(copyFlag):
        print("exporting\n")
        count_images = count_images + 1
        count_car = count_car + temp_car_count
        count_person = count_person + temp_person_count
        count_bicycle = count_bicycle + temp_bicycle_count
        #copy(label_file_path, labels_output_path)
        #copy(imgs_file_path, imgs_output_path)
        #copy(annotations_file_path, annotations_output_path)
    #clear temp counts
    temp_person_count = 0
    temp_car_count = 0
    temp_bicycle_count = 0
    label_data.close()
print("num of cars: ")
print(count_car)
print("num of person: ")
print(count_person)
print("num of bicycle: ")
print(count_bicycle)
