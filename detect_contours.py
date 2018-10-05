import argparse
import cv2

# Take a path to an image as an argument
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image.")
args = vars(ap.parse_args())
# Import image with cv2
img = cv2.imread(args["image"])
# Create copy of original. Contour func manipulates image.
orig = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17)
edged = cv2.Canny(gray, 30, 200)
# Find contours in image, keep largest.
_, contours, _ = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
# Initialize egg contour and area of contour
egg_contour = None
contour_area = None

for contour in contours:
    # Approximate contour
    perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.000001 * perimeter, True)
    # Bounding rect.
    x, y, w, h = cv2.boundingRect(contour)

    if w > 500 and h > 500:
        cropped_img = img[y:y+h, x:x+w]
        _, thresh_cropped_img = cv2.threshold(cropped_img, 40, 255, cv2.THRESH_BINARY)
        cv2.imshow("Threshold: Cropped Image", thresh_cropped_img)
        cv2.imshow("Cropped Image", cropped_img)
        cv2.waitKey(0)

    if len(approx) > 0:
        contour_area = cv2.contourArea(contour)
        egg_contour = approx
        print(contour_area)
        break

cv2.drawContours(img, [egg_contour], -1, (0, 255, 0), 3)
cv2.imshow("Canny", edged)
cv2.imshow("Contour", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
