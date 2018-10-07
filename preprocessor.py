from time import time
import cv2
import numpy as np

# Record time so time elapsed may be presented.
start_time = time()
# Import image and cvt to gray.
img = cv2.imread('images/edge_stacks/5ml/5.32.tif')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Record height and width of img.
h, w, _ = img.shape
# Initialize empty list for coordinates to be saved.
color_coords = []


for x in range(1, w - 1):
    for y in range(1, h - 1):
        if np.any(img[y, x] > 13):
            color_coords.append([y, x])

end_time = time()  # Record process end time.


def x_coordinate(item):  # Returns x coordinate from passed list.
    return item[1]


def y_coordinate(item):  # Returns y coordinate from passed list.
    return item[0]


x_sorted = sorted(color_coords, key=x_coordinate)
y_sorted = sorted(color_coords, key=y_coordinate)
# Min and Max values of both x and y from
low_x = x_sorted[0][1]
high_x = x_sorted[-1][1]
low_y = y_sorted[0][0]
high_y = y_sorted[-1][0]

print("Low x-coordinate: " + str(low_x)
      + "\nHigh x-coordinate: " + str(high_x)
      + "\nLow y-coordinate: " + str(low_y)
      + "\nHigh y-coordinate: " + str(high_y)
      + "Process run time: " + str(end_time - start_time))
