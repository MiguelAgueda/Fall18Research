import cv2
import argparse

# from matplotlib import pyplot as plt


ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image',
                type=str,
                help="System path to image file.",
                required=True)
args = vars(ap.parse_args())
img = cv2.imread(args['image'])
orig = img
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17)


def nothing(x):
    pass


cv2.namedWindow('image')
cv2.createTrackbar('Canny_1', 'image', 0, 300, nothing)
cv2.createTrackbar('Canny_2', 'image', 0, 1000, nothing)

while True:
    cv2.imshow("image", img)
    cv2.imshow("orig", orig)
    k = cv2.waitKey(1) & 0xFF

    if k == 27:
        break

    canny_1 = cv2.getTrackbarPos('Canny_1', 'image')
    canny_2 = cv2.getTrackbarPos('Canny_2', 'image')
    img = cv2.Canny(gray, canny_1, 0)

cv2.destroyAllWindows()
