import numpy as np
import math
import matplotlib.pyplot as plt
from location_points import location_points

def connect_check(x1,y1,x2,y2,size):
    min_distance = size
    for i in range(0, 8):
        for j in range(0, 8):
            x11 = x1[i]
            y11 = y1[i]
            x22 = x2[j]
            y22 = y2[j]
            target = (((x11 - x22) ** 2)+((y11 - y22) ** 2)) ** 0.5
            if target < min_distance:
                min_distance = target
    if min_distance < math.log10(size):
        return 1
    else:
        return 0
img1 = np.loadtxt('./result_maskrcnn/switch1', dtype=np.uint8)  #dtype=np.float32
img2 = np.loadtxt('./result_maskrcnn/switch2', dtype=np.uint8)  #dtype=np.float32
size = min(img1.shape[0],img2.shape[1])
location_x1, location_y1 = location_points(img1)
location_x2, location_y2 = location_points(img2)
result = connect_check(location_x1, location_y1,location_x2, location_y2, size)
img = np.zeros(img1.shape, dtype=int)
for i in range(0, img1.shape[0]):
    for j in range(0, img2.shape[1]):
        if img1[i][j] == 1 and img2[i][j] == 1:
            img[i][j] = 3
            result = 1
        elif img2[i][j] == 1:
            img[i][j] = 2
        elif img1[i][j] == 1 :
            img[i][j] = 1
if result == 1:
    plt.matshow(img, cmap=plt.get_cmap('Greens'), alpha=0.8)  # , alpha=0.3
    plt.text(25, 28, 'isolate is close')
    plt.show()
else:
    plt.matshow(img, cmap=plt.get_cmap('Greens'), alpha=0.8)  # , alpha=0.3
    plt.text(25, 28, 'isolate is open')
    plt.show()


