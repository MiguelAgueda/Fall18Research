import cv2
import argparse


def nothing(x):
    pass


def binary_thresh(image):
    cv2.namedWindow('Binary Threshold')
    cv2.createTrackbar('Threshold Value', 'Binary Threshold', 0, 255, nothing)
    k1 = 0
    while k1 != 27:
        k1 = cv2.waitKey(1)
        binary_thresh_val = cv2.getTrackbarPos('Threshold Value', 'Binary Threshold')
        _, binary_thresh_img = cv2.threshold(image,
                                         binary_thresh_val,
                                         255,
                                         cv2.THRESH_BINARY)
        cv2.imshow('Binary Threshold', binary_thresh_img)


def gaussian_thresh(image):
    cv2.namedWindow('Gaussian Threshold')
    cv2.createTrackbar('threshold', 'Gaussian Threshold', 0, 255, nothing)
    cv2.createTrackbar('Save', 'Binary Threshold', 0, 1, nothing)
    k2 = 0
    while k2 != 27:
        k2 = cv2.waitKey(1)
        gaussian_thresh_val = cv2.getTrackbarPos('threshold', 'Gaussian Threshold')
        gaussian_thresh_img = cv2.adaptiveThreshold(image,
                                                    255,
                                                    # block_size,
                                                    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                    cv2.THRESH_BINARY_INV,
                                                    11,
                                                    gaussian_thresh_val)
        cv2.imshow('Gaussian Threshold', gaussian_thresh_img)


def mean_thresh(image):
    cv2.namedWindow('Mean Threshold')
    cv2.createTrackbar('threshold', 'Mean Threshold', 0, 20, nothing)
    k3 = 0
    while k3 != 27:
        k3 = cv2.waitKey(1)
        mean_thresh_val = cv2.getTrackbarPos('threshold', 'Mean Threshold')
        mean_thresh = cv2.adaptiveThreshold(image,
                                            255,
                                            cv2.ADAPTIVE_THRESH_MEAN_C,
                                            cv2.THRESH_BINARY,
                                            9,
                                            mean_thresh_val)
        cv2.imshow('Mean Threshold', mean_thresh)


def to_zero_thresh(image):
    cv2.namedWindow('To Zero Threshold')
    cv2.createTrackbar('threshold', 'To Zero Threshold', 0, 255, nothing)
    k4 = 0
    while k4 != 27:
        k4 = cv2.waitKey(1)
        to_zero_thresh_val = cv2.getTrackbarPos('threshold', 'To Zero Threshold')
        _, to_zero_thresh_img = cv2.threshold(image, to_zero_thresh_val, 255, cv2.THRESH_TOZERO)
        cv2.imshow('To Zero Threshold', to_zero_thresh_img)
        if k4 == 129:
            cv2.imwrite('images/cropped_images/thresh_img.png', image)
        else:
            continue


def cli_menu(image):
    running = True
    while running:
        error = "Invalid input"
        choice = input("""
        \n\tThis application is designed to help you choose a threshold
        value for image processing. Choose your desired threshold process(Default = 1).
        To exit image view at any time, press esc.
        \n\t1: Binary Threshold\n\t2: Gaussian Threshold\n\t3: Mean Threshold
        4: Threshold To Zero
        \n\t9: Quit\n\n\t> """)
        if choice == '1':
            binary_thresh(image)
        elif choice == '2':
            gaussian_thresh(image)
        elif choice == '3':
            mean_thresh(image)
        elif choice == '4':
            to_zero_thresh(image)
        elif choice == '9':
            running = False
        else:
            print(error)


ap = argparse.ArgumentParser()
parser = argparse.ArgumentParser()
ap.add_argument('-i', '--image',
                type=str,
                required=False,
                help="Path to an image.")
args = vars(ap.parse_args())
image = cv2.imread(args['image'], 0)
cli_menu(image)
