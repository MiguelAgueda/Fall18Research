import cv2
import os
from tune_image import TuneImageSettings


tis = TuneImageSettings()
path = "C:\\Users\\migue\\Documents\\PyCharmProjects\\fall18research\\images\\split_5ml\\"


def get_contours(filename):
    full_path = path + filename
    im = cv2.imread(full_path, 0)
    _, thresh = cv2.threshold(im, tis.thresh_val, 255, 0)
    _, bin_thresh = cv2.threshold(im, 0, 255, cv2.THRESH_BINARY)
    _, cnts, _ = cv2.findContours(bin_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnt = sorted(cnts, key=cv2.contourArea, reverse=True)[:1]
    return cnt, filename


def processor():
    for filename in os.listdir():
        contours = get_contours(filename)
        for contour in contours:
            mnt = cv2.moments(contour)
            area = int(mnt['m00'])
            return area
