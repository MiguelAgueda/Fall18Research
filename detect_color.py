# Code example from https://www.pyimagesearch.com/2014/08/04/opencv-python-color-detection/
import numpy as np
import argparse
import cv2


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help="path to the image.")
args = vars(ap.parse_args())


image = cv2.imread(args["image"])
boundaries = [
    ([13, 13, 13], [255, 255, 255]),
]

for (lower, upper) in boundaries:
    # Create numpy arrays from the boundaries
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")

    # find the colors within the specified boundaries and
    # find the mask
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask=mask)

    cv2.imshow("image", image)
    cv2.imshow("output", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
