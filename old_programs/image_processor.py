import os
import cv2
import numpy as np
from tune_image import TuneImageSettings

tis = TuneImageSettings()


def process_images():
    path = "C:\\Users\\migue\\Documents\\PyCharmProjects\\fall18research\\images\\split_5ml\\"

    for filename in os.listdir(path):
        src = path + filename
        img = cv2.imread(src)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.bilateralFilter(gray, 11, 17, 17)
        edged = cv2.Canny(gray, 30, 200)
        # Find contours in image, keep largest.
        _, contours, _ = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:1]

        for contour in contours:
            perimeter = cv2.arcLength(contour, True)  # Approximate contour
            approx = cv2.approxPolyDP(contour, 0.000001 * perimeter, True)
            x, y, w, h = cv2.boundingRect(contour)  # Get dimensions of a bounding rectangle.
            cropped_img = img[y:y + h, x:x + w]  # Crop image using bounding rectangle.

            # Start the counting of pixels to provide white to black px ratio
            white_px_count = 0
            image_area = w * h
            contour_area = cv2.contourArea(contour)  # Giving inaccurate values.
            # print(contour_area)  # Print area of contour to console.
            _, to_zero_thresh_inv_img = cv2.threshold(cropped_img,
                                                      tis.thresh_value,
                                                      255,
                                                      cv2.THRESH_TOZERO_INV)  # Apply an inverse to-zero threshold to image.
            _, to_zero_thresh_img = cv2.threshold(to_zero_thresh_inv_img,
                                                  tis.inv_thresh_value,
                                                  255,
                                                  cv2.THRESH_TOZERO)  # Apply a to-zero threshold to image.
            thresh_cropped_height, thresh_cropped_width, _ = to_zero_thresh_img.shape  # Get size of image.

            # Loop through pixels in image and count the ones which are white.
            for x in range(1, thresh_cropped_width - 1):
                for y in range(1, thresh_cropped_height - 1):
                    if np.any(to_zero_thresh_img[y, x] > 35):
                        white_px_count += 1

        white_total_px_ratio = white_px_count / image_area  # Math
        white_total_px_percentage = white_total_px_ratio * 100  # Math

        # Print collected data to console.
        print("""\n
        Image: {name}
        Number of white pixels: {white_px} px
        Area of image: {area} px
        Area of contour: {contour_area} px
        Percentage of white to total pixels: {percent}%
        """.format(name=src,
                   white_px=white_px_count,
                   area=image_area,
                   contour_area=contour_area,
                   percent=white_total_px_percentage))

    print("Done")
    quit()
