import numpy 
import cv2 as cv

img_file = 'image/tomboy.jpeg'
# Read the given image file
img = cv.imread(img_file)
# Check whether the image is valid or not
if img is not None:
    # Show the image
    cv.imshow('Image Viewer', img)
    cv.waitKey()
    cv.destroyAllWindows()