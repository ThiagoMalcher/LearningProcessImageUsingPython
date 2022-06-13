#Autor: Thiago Malcher
#baseaded iin https://www.geeksforgeeks.org/python-intensity-transformation-operations-on-images/

import cv2
import numpy as np

def stretchingLinear(pathImageTouse, pathImageTosave):

    # Open the image.
    img = cv2.imread(pathImageTouse)
    blur = cv2.GaussianBlur(img, (7, 7), 0)  # aplica blur
    # Apply log transform.
    c = 255 / (np.log(1 + np.max(blur)))
    log_transformed = c * np.log(1 + blur)

    # Specify the data type.
    log_transformed = np.array(log_transformed, dtype=np.uint8)

    # Save the output.
    cv2.imwrite(pathImageTosave,log_transformed)
    return "SUCESS"

def stretchingLinearParts(pathImageTouse, pathImageTosave):

    def pixelVal(pix, r1, s1, r2, s2):
        if (0 <= pix and pix <= r1):
            return (s1 / r1) * pix
        elif (r1 < pix and pix <= r2):
            return ((s2 - s1) / (r2 - r1)) * (pix - r1) + s1
        else:
            return ((255 - s2) / (255 - r2)) * (pix - r2) + s2

    # Open the image.
    img = cv2.imread(pathImageTouse)
    blur = cv2.GaussianBlur(img, (7, 7), 0)  # aplica blur
    # Define parameters.
    r1 = 70
    s1 = 0
    r2 = 140
    s2 = 255

    # Vectorize the function to apply it to each value in the Numpy array.
    pixelVal_vec = np.vectorize(pixelVal)

    # Apply contrast stretching.
    contrast_stretched = pixelVal_vec(blur, r1, s1, r2, s2)

    # Save edited image.
    cv2.imwrite(pathImageTosave, contrast_stretched)
    return "SUCESS"

def stretchingLogarithm(pathImageUse, saveImage):

    img = cv2.imread(pathImageUse)
    blur = cv2.GaussianBlur(img, (7, 7), 0)  # aplica blur
    c = 255 / (np.log(1 + np.max(img)))
    log_transformed = c * np.log(1 + blur)

    # Specify the data type.
    log_transformed = np.array(log_transformed, dtype=np.uint8)


    cv2.imwrite(saveImage, log_transformed)

    cv2.imshow('log_transformed', log_transformed)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 0

def stretchingQuadratic():
    return 0

def stretchingExponential():
    return 0