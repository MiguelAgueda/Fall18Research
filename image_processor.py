import cv2
import os
import argparse
import numpy as np


ap = argparse.ArgumentParser()
ap.add_argument('-d', '--directory',
                type=str,
                help="Path to directory with files.",
                required=True)
# ap.add_argument('-D', '--destination',
#                 type=str,
#                 help="Path to destined directory.",
#                 required=True)
# ap.add_argument('-t', '--file_type',
#                 type=str,
#                 help="File type (.png, .tif, .txt, .py, etc.)",
#                 required=True)
args = vars(ap.parse_args())
path = args['directory']
# destination = args['destination']
# file_type = args['file_type']

for filename in os.listdir(path):
    src = path + filename
    img = cv2.imread(src)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    edged = cv2.Canny(gray, 30, 200)
    # Find contours in image, keep largest.
    _, contours, _ = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

    # egg_contour = None
    # contour_area = None

    for contour in contours:
        # Approximate contour
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.000001 * perimeter, True)
        # Bounding rect.
        x, y, w, h = cv2.boundingRect(contour)

        if w > 100 and h > 100:
            cropped_img = img[y:y+h, x:x+w]
            # Threshold the now cropped image
            _, thresh_cropped_img = cv2.threshold(cropped_img,
                                                  40,
                                                  255,
                                                  cv2.THRESH_BINARY)
            # cv2.imshow("Threshold: Cropped Image", thresh_cropped_img)
            # cv2.imshow("Cropped Image", cropped_img)
            # try:
            #     cv2.imwrite(destination, cropped_img)
            # except cv2.error:
            #     print("Image not written to disk: " + filename)
            #     continue

            # nothing to show, nothing to wait for.
            # cv2.waitKey(0)

    # Start the counting of pixels to provide white to black px ratio
        white_px_count = 0
        total_px_count = cv2.contourArea(contour)  # Total px in contour

        _, to_zero_inv_img = cv2.threshold(cropped_img,
                                           144, 255,
                                           cv2.THRESH_TOZERO_INV)
        thresh_cropped_height, thresh_cropped_width, _ = to_zero_inv_img.shape
        for x in range(1, thresh_cropped_width - 1):
            for y in range(1, thresh_cropped_height - 1):
                if np.any(to_zero_inv_img[y, x] > 35):
                    white_px_count += 1

    white_black_px_ratio = white_px_count / total_px_count
    # white_black_px_percentage = white_black_px_ratio * 100
    print("""\n
    Image: {name}
    Number of White Pixels: {white_px} px
    Area of Contour: {area} px
    Percentage of White Pixels: {ratio}%
    """.format(name=src,
               white_px=white_px_count,
               area=total_px_count,
               # percent=white_black_px_percentage,
               ratio=white_black_px_ratio))
    # White-Black Pixel Ratio: {ratio}
