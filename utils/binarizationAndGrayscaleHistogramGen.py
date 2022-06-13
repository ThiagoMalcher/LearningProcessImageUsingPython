#Autor: Thiago Malcher
import cv2
import matplotlib
import numpy as np
import skimage.color
import skimage.io
import matplotlib.pyplot as plt

'''
* method using ppm image
I just turned it to gray, the binarization will take a long time
In this method it is necessary to read all the information from the original image,
thus storing it in a vector to then generate a new image with gray scale,
so every 3 values of the vector is equivalent to RGB, where when discovering the 3 values
it is calculated for switch to zinc and thus save a new rgb line in the new image.
to ensure that the value position changes with each discovery, I removed the value from position 0. 
OBS: if you want to change the ppm file, set the variable that is in main.py
'''

def methodUsingPpmImage(pathImage, pathImageSave):

    imageOriginal = open(pathImage)
    typeimg = ' '.join(map(str, imageOriginal.readline().splitlines()))
    width, heigth = imageOriginal.readline().split()
    RGB = ' '.join(map(str, imageOriginal.readline().splitlines()))
    data = imageOriginal.read().split()

    # create a new image
    pathImageSave 
    save = open(pathImageSave, "w")
    save.write(str(typeimg + "\n"))
    save.writelines(str(width + " " + heigth + "\n"))
    save.writelines(str(RGB + "\n"))

    # local variables
    red, green, blue, count = 0, 0, 0, 0
    numbersTochange = len(data)

    # This process is better in c++!
    # the beginning of the vector is R then comes G and B, but for that I always delete the position 0 of the vector and so i do three for to get the respective values
    while (count < numbersTochange):
        count += 1
        # discovery red
        for values in data:
            del data[0]
            red = int(values)
            if red + 50 >= 255:
                red = 255
            else:
                red += 50
            break
        # discovery green
        for values in data:
            del data[0]
            green = int(values)
            if green + 50 >= 255:
                green = 250
            else:
                green += 50
            break
        # discovery blue
        for values in data:
            del data[0]
            blue = int(values)
            if blue + 50 >= 255:
                blue = 255
            else:
                blue += 50
            break
        #Transforme to gray
        imgGray = 0.2989 * red + 0.5870 * green + 0.1140 * blue
        red = int(imgGray)
        green = int(imgGray)
        blue = int(imgGray)
        save.writelines(str(str(red) + " " + str(green) + " " + str(blue)) + "\n")

    save.close()
    return "SUCESS"

def methodUsingImread(pathImage, pathImageSave):

    img = cv2.imread(pathImage)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    suave = cv2.GaussianBlur(img, (7, 7), 0)  # aplica blur
    (T, bin) = cv2.threshold(suave, 160, 255, cv2.THRESH_BINARY)
    (T, binI) = cv2.threshold(suave, 160, 255,
                              cv2.THRESH_BINARY_INV)
    resultado = np.vstack([
        np.hstack([img, suave, bin]),
      #  np.hstack([binI, cv2.bitwise_and(img, img, mask=binI)])
    ])
    cv2.imshow("Binarização da imagem", resultado)
    cv2.waitKey(0)
    histogramGen(pathImage)
    return 0


def histogramGen(pathimg):
    #reference: https://datacarpentry.org/image-processing/05-creating-histograms/
    # read the image of a plant seedling as grayscale from the outset
    image = skimage.io.imread(fname=pathimg, as_gray=True)

    # display the image
    fig, ax = plt.subplots()
    plt.imshow(image, cmap="gray")
    #plt.show()
    histogram, bin_edges = np.histogram(image, bins=256, range=(0, 1))
    # configure and draw the histogram figure
    plt.figure()
    plt.title("Grayscale Histogram")
    plt.xlabel("grayscale value")
    plt.ylabel("pixel count")
    plt.xlim([0.0, 1.0])  # <- named arguments do not work here

    plt.plot(bin_edges[0:-1], histogram)  # <- or here
    plt.show()
