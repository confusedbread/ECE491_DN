import os
import sys

base_path = 'ECE491_DN-master/data/491data/'
i = 1000
with open("iou.sh", "w") as fh:
  while i <= 12000:
      cmd = './darknet detector recall {}491.data {}491_yolov3-tiny.cfg ECE491_DN-master/backup/Plus_Firetruck/491_yolov3-tiny_{}.weights'.format(base_path, base_path, i)
      fh.write(cmd + '\n')
      i = i + 1000
  cmd = './darknet detector recall {}491.data {}491_yolov3-tiny.cfg ECE491_DN-master/backup/Plus_Firetruck/491_yolov3-tiny_final.weights'.format(base_path, base_path)
  fh.write(cmd + '\n')
