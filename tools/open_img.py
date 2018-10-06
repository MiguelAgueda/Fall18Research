import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help="path to the image.")
args = vars(ap.parse_args())
img = cv2.imread(args["image"])
cv2.imshow('', img)

cv2.waitKey(0)
cv2.destroyAllWindows()