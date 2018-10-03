import cv2
import numpy as np
import argparse


# Construct arguments, --image is used as path to image arg.
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# Load image
image = cv2.imread(args["image"])
# Clone image for output
output = image.copy()
# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detecting circles
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.5, 10)

# Ensure some circles were detected
if circles is not None:
    # Convert the (x, y) coords and radius of the circles to ints
    circles = np.round(circles[0, :]).astype("int")
    # Loop over the (x, y) coords and radius of the circles
    for (x, y, r) in circles:
        # Draw the circle in the output image, then draw a rectangle
        # corresponding to the center of the circle
        cv2.circle(output, (x, y), r, (0, 255, 0), 4)
        cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

    cv2.imshow("image", np.hstack([image, output]))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("No circles detected.")
