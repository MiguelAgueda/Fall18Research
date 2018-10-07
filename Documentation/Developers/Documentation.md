# Research Image Tools
This project aims to help researchers standardize image processing for
the extraction of data by bundling several open source tools into simple commands.

## Reasons for method usage
### detect_countours.py
Sources:
https://docs.opencv.org/3.1.0/dd/d49/tutorial_py_contour_features.html

- argparse is used to accept a path to an image from the command line. 
- cv2.imread loads the image so that it may be processed.
- cv2.cvtColor converts the BGR image into a Grayscale image.
Improves processing time.
- cv2.bilateralFilter is an efficient method for applying a blur to an image.
The effect of this are smooth edges in the image.
- cv2.Canny is a method that is used to find all the edges / contours in ab image. 
- cv2.arcLength is used to measure the length of an arc. Can also be used
to measure the perimeter of a closed contour. 
- cv2.approxPolyDP is a method for approximating the shape of a contour.
- cv2.boundingRect is used to find the smallest rectangle needed to enclose
the contour. The contents of the bounding rectangle will be cropped from the image.




