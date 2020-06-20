# From Python
# It requires OpenCV installed for Python
import sys
import cv2
import os
from sys import platform
import argparse

import pickle
import numpy as np

def data_flip(data):
  flip_vec = (0, 1, 5, 6, 7, 2, 3, 4, 8, 12, 13, 14, 9, 10, 11, \
    16, 15, 18, 17, 22, 23, 24, 19, 20, 21)
  fliped_data = []
  for i in range(25):
    fliped_data.append(data[flip_vec[i]])
  return fliped_data

with open('poses.pickle', 'rb') as f:
  outdata = pickle.load(f)

width = 2048
height = 1024

angle_seq = (0, 30, 60, 90, -90, -120, -150, -180)
#angle_seq = (180, 210, 240, 270, 90, 60, 30, 0)
normed_data = []

tmp = np.array(outdata[1])
print(type(tmp))
print(len(tmp[0][0]))
print(len(tmp[0][0][0]))
# print(tmp)
tmp = np.squeeze(tmp)
print(tmp.shape)
print('outdata', len(outdata))
for i, seq in enumerate(outdata):
  print(i)
  # print(seq)
  # print('seq', len(seq))
  normed_seq = []
  fliped_seq = []
  for dataa in seq:
#    print(len(dataa))
#    canvas = np.zeros((height, width, 3), np.uint8)
#    canvas = draw_bodypose(canvas, data)
#    print(dataa[0])
    data = dataa[0]
#    print(data)
    minx = 100
    maxx = 0
    miny = 99999
    maxy = -99999
    for j in range(25):
      if data[j][2] == 0.0:
        continue
      else:
        x, y = data[j][0:2]
        if x > maxx:
          maxx = x
        elif x  < minx:
          minx = x
        if y > maxy:
          maxy = y
        elif y  < miny:
          miny = y

    if data[8][2]!= 0.0:
      midx = data[8][0] #(maxx - minx)/2
      midy = data[8][1] #(maxy - miny)/2
    elif data[9][2] != 0.0 and data[12][2] != 0.0:
      midx = (data[8][0] + data[12][0])/2
      midy = (data[8][1] + data[12][1])/2
    else:
      #print('no hip node')
      continue

    widthx = maxx - minx
    widthy = maxy - miny

    normed_single =[]
    fliped_single = []
    for j in range(25):
      if data[j][2] == 0.0:
        xtmp = 0.0
        ytmp = 0.0
      else:
        xtmp = (data[j][0]-midx)/widthy
        ytmp = (data[j][1]-midy)/widthy

      normed_single.append([xtmp, ytmp, data[j][2]])
      fliped_single.append([-xtmp, ytmp, data[j][2]])
    normed_seq.append([normed_single, angle_seq[i]])
    fliped_seq.append([data_flip(fliped_single), -angle_seq[i]])
  normed_data.append(normed_seq)
  normed_data.append(fliped_seq)

print(len(normed_data[0]))
with open('normed_poses.pickle', 'wb') as f:
  pickle.dump(normed_data, f)

#    cv2.imshow('window', canvas)
#    key =cv2.waitKey(50)

#    if key &0xff == ord('q'):
#      break

#plt.imshow(canvas[:, :, [2, 1, 0]])
#plt.axis('off')
#plt.show()

#cv2.destroyAllWindows()
