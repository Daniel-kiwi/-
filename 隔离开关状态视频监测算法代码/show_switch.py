import numpy as np
import math
import matplotlib.pyplot as plt
from location_points import location_points

img1 = np.loadtxt('./result_maskrcnn/switch2', dtype=np.uint8)  #dtype=np.float32
plt.matshow(img1, cmap=plt.get_cmap('Greens'), alpha=0.8)  # , alpha=0.3
plt.text(25, 28, 'yes')
plt.show()


