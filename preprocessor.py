import cv2
import numpy as np

true_px = 0
img = cv2.imread('images/edge_stacks/5ml/5.32.tif')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# h, w = gray.shape
h, w, c = img.shape
total_px = h * w

for x in range(1, w + 1):
    for y in range(1, h + 1):
        print("Searching ...")
        if np.any(img[x, y] > 13):
            true_px += 1
            print(x, y)

print("Done searching.")
percent_px = (true_px / total_px) * 100
print(percent_px)
