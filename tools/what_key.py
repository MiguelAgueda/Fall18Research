import cv2


img = cv2.imread('C:/Users/migue/Documents/PyCharmProjects/fall18research/images/split_5ml/5.03.1.PNG')
cv2.namedWindow('win')
key = 0
while key != 27:
    key = cv2.waitKey(0)
    print(key)
    cv2.imshow('win', img)

