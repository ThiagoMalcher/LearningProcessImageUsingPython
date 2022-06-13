import cv2
import numpy as np
from matplotlib import pyplot as plt


def equalizationHistogram(pathImage, pathImageSave, histo):

    img = cv2.imread(pathImage, 0)
    plt.hist(img.ravel(), 256, [0, 256])

    plt.show()
    plt.savefig('hist.png')

    equ = cv2.equalizeHist(img)
    res = np.hstack((img, equ))

    cv2.imshow('Equalized Image', res)
    cv2.imwrite(pathImageSave, res)

    plt.hist(res.ravel(), 256, [0, 256])

    plt.show()
    plt.savefig(histo)