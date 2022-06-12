#These scripts are to perform the resolution of the impact-lab course questions
#impact-lab - Manaus - AM - Brazil
import os

print("#########################################################")
print("###############-Learning image processing-###############")
print("###############-Autor: Thiago Malher-####################")
print("############-Contact: malcher.tm@gmail.com-##############")
print("#########################################################")

print("##################-Select Option to run-#################")
from utils.binarizationAndGrayscaleHistogramGen import methodUsingPpmImage

menu = {}
menu['1']="Image binarization and grayscale image histogram generation."
menu['2']="Delete Student."
menu['3']="Find Student"
menu['4']="Exit"

action = {}
action['1']="Method using file ppm"
action['2']="Method using imread"

while True:
  options=menu.keys()
  for keyvalues in options:
      print(keyvalues, menu[keyvalues])

  optionSelected = input("Please Select:")
  break

if optionSelected == '1':
    while True:
        getAction = action.keys()
        for response in getAction:
            print(response, action[response])

        actionSelected = input("Please Select method:")
        break
    if actionSelected == "1":
        # you can change file ppm, this files stay in filesPPM in project
        pathOs = os.getcwd()
        pathImage = pathOs + r"\filesPPM\apollo.ppm"
        pathImageSave = pathOs + r"\filesPPM\Result\result.ppm"
        res = methodUsingPpmImage(pathImage, pathImageSave)
        if res == "SUCESS":
            print('SUCESS PROCESS USING PPM FILE')
        else:
            print('FAILURE: PROCESS USING PPM FILE')
elif optionSelected == '2':
    print("other question")
elif optionSelected == '3':
    print("other ")


