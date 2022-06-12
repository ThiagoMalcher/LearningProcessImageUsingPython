#Autor: Thiago Malcher
'''
* method using ppm image
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
                green = 255
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
        imgGray = 0.2989 * red + 0.5870 * green + 0.1140 * blue
        red = int(imgGray)
        green = int(imgGray)
        blue = int(imgGray)
        save.writelines(str(str(red) + " " + str(green) + " " + str(blue)) + "\n")

    save.close()
    return "SUCESS"

def methodUsingImread():
    return 0