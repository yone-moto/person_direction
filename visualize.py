# From Python
# It requires OpenCV installed for Python
import sys
import cv2
import os
from sys import platform
import argparse

import pickle
import numpy as np
import matplotlib as plt

def draw_bodypose(canvas, data):
  stickwidth = 1
#    limbSeq = [[2, 3], [2, 6], [3, 4], [4, 5], [6, 7], [7, 8], [2, 9], [9, 10], \
#               [10, 11], [2, 12], [12, 13], [13, 14], [2, 1], [1, 15], [15, 17], \
#               [1, 16], [16, 18], [3, 17], [6, 18], \
  limbSeq = [[2, 3], [3, 4], [6, 7], [9, 10], \
               [10, 11], [12, 13], [13, 14], [2, 1], [1, 15], [15, 17], \
               [1, 16], [16, 18], \
                 [8, 9], [1, 8], [8, 12], [1, 5], [5, 6],\
                   [14, 21], [20, 21], [14, 20], [19, 20], \
                     [11, 24], [23, 24], [11, 23], [22, 23]]

  colors = [[255, 0, 0], [255, 85, 0], [255, 170, 0], [255, 255, 0], [170, 255, 0], [85, 255, 0], [0, 255, 0], \
              [0, 255, 85], [0, 255, 170], [255, 255, 255], [0, 170, 255], [0, 85, 255], [0, 0, 255], [85, 0, 255], \
              [170, 0, 255], [255, 0, 255], [255, 0, 170], [255, 0, 85], \
                [255, 0, 0], [255, 85, 0], [255, 170, 0], [255, 255, 0], [170, 255, 0], [85, 255, 0], [0, 255, 0]]

  mag = 200
  for d in data:
    for i in range(25):
#      print(d[i])
      if d[i][2] > 0.2:
        x, y = d[i][0:2]
        x = x +0.5
        y = y +0.5
        cv2.circle(canvas, (int(x*mag), int(y*mag)), 3, colors[i], thickness=1) #-1)

    for pair in limbSeq:
#      print(pair)
#      print(d[pair[0]][:2], d[pair[1]][:2])
      if d[pair[0]][2] > 0.2 and d[pair[1]][2] > 0.2:
        x1, y1 = d[pair[0]][0:2]
        x2, y2 = d[pair[1]][0:2]
        x1 = x1 +0.5
        y1 = y1 +0.5
        y2 = y2 +0.5
        x2 = x2 +0.5
        cv2.line(canvas, (int(x1*mag), int(y1*mag)), (int(x2*mag), int(y2*mag)), (255, 255, 255), thickness=1, lineType=cv2.LINE_4)

    return canvas

with open('normed_poses_tread.pickle', 'rb') as f:
  outdata = pickle.load(f)

width = 2048
height = 1024

for seq in outdata:
  # print(seq)
  for data in seq:
    print(data)
    canvas = np.zeros((height, width, 3), np.uint8)
    canvas = draw_bodypose(canvas, data)

    cv2.imshow('window', canvas)
    key =cv2.waitKey()

    if key &0xff == ord('q'):
      break
  if key &0xff == ord('q'):
    break
  

# plt.imshow(canvas[:, :, [2, 1, 0]])
# plt.axis('off')
# plt.show()

cv2.destroyAllWindows()
