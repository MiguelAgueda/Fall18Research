import cv2
import argparse
import numpy as np


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image",
                required=True,
                help="Path to image.")
# Import image and cvt to gray.
img = cv2.imread('images/edge_stacks/5ml/5.32.tif')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Record height and width of img.
h, w, _ = img.shape
white_px_count = 0


for x in range(1, w - 1):  # Loop through every pixel
    for y in range(1, h - 1):  # and check its color value
        if np.any(img[y, x] > 13):  # to count it as 1 or 0
            white_px_count += 1


print("""
Total pixels in image: {h * w}
Total white pixels: {wt_ct}
Area of contour: """.format(h=h, w=w, wt_ct=white_px_count))
