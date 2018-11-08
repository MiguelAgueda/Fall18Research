import cv2
import os
import argparse
import numpy as np


# ap = argparse.ArgumentParser()
# ap.add_argument('-d', '--directory',
#                 type=str,
#                 help="Path to directory with files.",
#                 required=True)
# args = vars(ap.parse_args())
# path = args['directory']
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
        # Approximate contour
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.000001 * perimeter, True)
        # Bounding rect.
        x, y, w, h = cv2.boundingRect(contour)
        cropped_img = img[y:y + h, x:x + w]

    # Start the counting of pixels to provide white to black px ratio
        white_px_count = 0
        image_area = w * h
        contour_area = cv2.contourArea(contour)
        print(contour_area)
        _, to_zero_inv_img = cv2.threshold(cropped_img,
                                           170, 255,
                                           cv2.THRESH_TOZERO_INV)
        _, to_zero_thresh_img = cv2.threshold(to_zero_inv_img, 32, 255, cv2.THRESH_TOZERO)
        thresh_cropped_height, thresh_cropped_width, _ = to_zero_thresh_img.shape

        for x in range(1, thresh_cropped_width - 1):
            for y in range(1, thresh_cropped_height - 1):
                if np.any(to_zero_thresh_img[y, x] > 35):
                    white_px_count += 1

    white_total_px_ratio = white_px_count / image_area
    white_total_px_percentage = white_total_px_ratio * 100

    print("""\n
    Image: {name}
    Number of white pixels: {white_px} px
    Area of image: {area}
    Area of contour: {contour_area} px
    Percentage of white to total pixels: {percent}%
    """.format(name=src,
               white_px=white_px_count,
               area=image_area,
               contour_area=contour_area,
               percent=white_total_px_percentage))

print("Done")
quit()
