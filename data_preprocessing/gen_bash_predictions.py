import os
import sys

base_path = 'ECE491_DN-master/data/491data/'
t_ext = '.txt'
i = 1000
with open("predictions.sh", "w") as fh:
  while i <= 12000:
      output_dir = '/Users/Stevengrosz/darknet/weights_iter_{}'.format(i)
      print(output_dir)
      if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
      #test image of ambulance
      cmd = './darknet detector test {}491.data {}491_yolov3-tiny.cfg ECE491_DN-master/backup/491_yolov3-tiny_{}.weights data/491data/images/n02701002_5349.jpg -out weights_iter_{}/n02701002_5349_prediction'.format(base_path, base_path, i, i)
      fh.write(cmd + '\n')
      #test image of car
      cmd = './darknet detector test {}491.data {}491_yolov3-tiny.cfg ECE491_DN-master/backup/491_yolov3-tiny_{}.weights data/491data/images/000343.jpg -out weights_iter_{}/000343_prediction'.format(base_path, base_path, i, i)
      fh.write(cmd + '\n')
      #test image of person (x2)
      cmd = './darknet detector test {}491.data {}491_yolov3-tiny.cfg ECE491_DN-master/backup/491_yolov3-tiny_{}.weights data/491data/images/000388.jpg -out weights_iter_{}/000388_prediction'.format(base_path, base_path, i, i)
      fh.write(cmd + '\n')
      #test image of bicycle
      cmd = './darknet detector test {}491.data {}491_yolov3-tiny.cfg ECE491_DN-master/backup/491_yolov3-tiny_{}.weights data/491data/images/000819.jpg -out weights_iter_{}/000819_prediction'.format(base_path, base_path, i, i)
      fh.write(cmd + '\n')
      #test image of fire truck
      cmd = './darknet detector test {}491.data {}491_yolov3-tiny.cfg ECE491_DN-master/backup/491_yolov3-tiny_{}.weights data/491data/images/n03345487_133.jpg -out weights_iter_{}/n03345487_133_prediction'.format(base_path, base_path, i, i)
      i = i+1000
      fh.write(cmd + '\n')
  #test image of ambulance
  cmd = './darknet detector test {}491.data {}491_yolov3-tiny.cfg ECE491_DN-master/backup/491_yolov3-tiny_final.weights data/491data/images/n02701002_5349.jpg -out weights_iter_final/n02701002_5349_prediction'.format(base_path, base_path)
  fh.write(cmd + '\n')
  #test image of car
  cmd = './darknet detector test {}491.data {}491_yolov3-tiny.cfg ECE491_DN-master/backup/491_yolov3-tiny_final.weights data/491data/images/000343.jpg -out weights_iter_final/000343_prediction'.format(base_path, base_path)
  fh.write(cmd + '\n')
    #test image of person (x2)
  cmd = './darknet detector test {}491.data {}491_yolov3-tiny.cfg ECE491_DN-master/backup/491_yolov3-tiny_final.weights data/491data/images/000388.jpg -out weights_iter_final/000388_prediction'.format(base_path, base_path)
  fh.write(cmd + '\n')
  #test image of bicycle
  cmd = './darknet detector test {}491.data {}491_yolov3-tiny.cfg ECE491_DN-master/backup/491_yolov3-tiny_final.weights data/491data/images/000819.jpg -out weights_iter_final/000819_prediction'.format(base_path, base_path)
  fh.write(cmd + '\n')
  #test image of fire truck
  cmd = './darknet detector test {}491.data {}491_yolov3-tiny.cfg ECE491_DN-master/backup/491_yolov3-tiny_final.weights data/491data/images/n03345487_133.jpg -out weights_iter_final/n03345487_133_prediction'.format(base_path, base_path)
  fh.write(cmd + '\n')
