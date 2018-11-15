import cv2
import numpy as np


class Circle(object):

    def __init__(self, image):
        # Perform all necessary actions on image.
        self.image = cv2.imread(image)
        self.output = self.image.copy()
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.new_filename = 0

    def detect_circles(self):
        """Detect all circles in an image,
        return the ratio of small circle diameter to large circle diameter."""
        # User hough circles to detect circles.
        circles = cv2.HoughCircles(self.gray, cv2.HOUGH_GRADIENT, 1.5, 70)

        # Ensure some circles were detected.
        if circles is not None:
            # Convert the (x, y) coordinates and radius of the circles to ints.
            circles = np.round(circles[0, :]).astype("int")
            # Loop over the (x, y) coordinates and radius of the circles.
            for (x, y, r) in circles:
                # Draw the circle in the output image, then draw a rectangle
                # corresponding to the center of the circle
                cv2.circle(self.output, (x, y), r, (0, 255, 0), 4)
                cv2.rectangle(self.output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

            # Create dynamic file names for display
            self.new_filename += 1
            cv2.imwrite("images/{}.png".format(self.new_filename), self.output)

        else:
            print("No circles detected.")

