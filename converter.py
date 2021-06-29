from os import write
import cv2 as cv
import numpy as np


img = cv.imread(r"Image-to-ASCII\images\swadha.jpg")
height, width = img.shape[0],img.shape[1]
print(img.shape)
img = cv.resize(img,(int(width*0.10),int(height*0.10)),interpolation=cv.INTER_AREA)
height, width = img.shape[0],img.shape[1]
print(img.shape)
img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ascii = ['@','#','S','%','?',"*",";",":","-","."]
st = ""
for i in range(height):
    for j in range(width):
        st += ascii[(img[i][j])//25] + " "
    st+="\n"
with open("Image-to-ASCII\\text.txt","w") as file:
    file.write(st)
print("done")

