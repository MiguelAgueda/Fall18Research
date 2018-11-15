import cv2


class TuneImageSettings:
    def __init__(self):
        self.thresh_val = 0
        self.inv_thresh_val = 0

    def nothing(self):
        pass

    def tune_zero_thresh(self, image):
        """Brings up a window with track bar to adjust threshold value."""
        cv2.namedWindow('To Zero Threshold')
        cv2.createTrackbar('threshold', 'To Zero Threshold', 0, 255, self.nothing)
        key = 0
        while key != 13:
            key = cv2.waitKey(1)
            self.thresh_val = cv2.getTrackbarPos('threshold', 'To Zero Threshold')
            _, to_zero_thresh_img = cv2.threshold(image, self.thresh_val, 255, cv2.THRESH_TOZERO)
            cv2.imshow('To Zero Threshold', to_zero_thresh_img)

    def tune_zero_inv_thresh(self, image):
        """Brings up a window with track bar to adjust threshold value."""
        cv2.namedWindow('To Zero Inverse Threshold')
        cv2.createTrackbar('threshold', 'To Zero Inverse Threshold', 0, 255, self.nothing)
        key = int
        while key != 13:
            key = cv2.waitKey(1)
            self.inv_thresh_val = cv2.getTrackbarPos('threshold', 'To Zero Inverse Threshold')
            _, to_zero_inv_thresh_img = cv2.threshold(image, self.inv_thresh_val, 255, cv2.THRESH_TOZERO_INV)
            cv2.imshow('To Zero Inverse Threshold', to_zero_inv_thresh_img)
