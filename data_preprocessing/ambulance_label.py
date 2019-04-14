import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

annotations_path = "/Users/Stevengrosz/darknet/data/491data/ambulanceData/Annotations"
labels_path = "/Users/Stevengrosz/darknet/data/491data/ambulanceData/labels"

classes = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor", "n02701002"]

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(annotations_path, labels_path):
    in_file = open(annotations_path, 'r')
    out_file = open(labels_path, 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        print("in for")
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            print("in cont")
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

ambulance_annotations = [os.path.join(annotations_path,fname) for fname in
              os.listdir(annotations_path) if fname.endswith('.xml')]

for annotation_file in ambulance_annotations:
    annotation_split = annotation_file.split('/')
    annotation_fileID = annotation_split[8]
    annotation_fileID = annotation_fileID[0:-4]
    annotations_file_path = str(annotation_file)
    label_file_path = labels_path + "/" + str(annotation_fileID) + ".txt"
    convert_annotation(annotations_file_path, label_file_path)
