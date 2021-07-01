import cv2 as cv
import numpy as np
from PIL import Image, ImageFont, ImageDraw

class Converter():
    def __init__(self, resizing_scale=0.10):
        """initialised the converter class by setting the neccesary variables"""

        path = r"Image-to-ASCII\images\roop.jpg"
        self.reszing_scale = resizing_scale 
        self.reading_img(path)
    
    
    def reading_img(self,path):
        """Reading the image from the given path"""

        img = cv.imread(path)
        height, width = img.shape[0],img.shape[1]
        print(f"Original image Dimenstions: height={img.shape[0]}px width={img.shape[1]}px channels={img.shape[2]}px")
        self.resizing(img,height,width)
    
    
    def resizing(self,img,height,width):
        """reszing the image so we don't get too big text file"""
        
        print("Resizing Image...")
        img = cv.resize(img,(int(width*self.reszing_scale),int(height*self.reszing_scale)),interpolation=cv.INTER_AREA)
        resized_height, resized_width = img.shape[0],img.shape[1]
        print(f"Resized image Dimenstions: height={img.shape[0]}px width={img.shape[1]}px channels={img.shape[2]}px")
        self.grayscaling(img,resized_height,resized_width)
    
    
    def grayscaling(self,img,height,width):
        """Graysclaing the image because we only need to deal with pixel intensities"""

        print("Graying the image...")
        grayed_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        self.converting_to_ascii(grayed_img,height,width)
    
    
    def converting_to_ascii(self, grayed_img,height,width):
        """Visiting each pixel of the resized gray image and converting it into
        a ASCII Character based on the pixel's intesity"""

        print("Converting to Characters...")
        ascii = ['@#','#S','S%','%?','??',"**",";;",":-","-.","..",".."]
        string = ""
        img_string = ""
        for i in range(height):
            for j in range(width):
                string += ascii[-(grayed_img[i][j])//25]
                img_string += ascii[-(grayed_img[i][j])//25]
            string+="\n"
        print("Finished converting...")
        self.writing_to_file(string)
        self.saving_image(img_string)
    
    
    def writing_to_file(self,string):
        """Writing the string to a text file so we can easily access it later"""

        print("Writing results to a text file")
        with open("text.txt","w") as file:
            file.write(string)
        
        print("Success!!!.. Enjoy the Masterpiece")
        # print(string)
        

    def saving_image(self,string):
        new_img = np.zeros((1280,720,3),dtype="uint8")
        # Make into PIL Image
        pil_img = Image.fromarray(new_img)

        # Get a drawing context
        draw = ImageDraw.Draw(pil_img)
        monospace = ImageFont.truetype("font.ttf",11)

        increment = 0
        y_increment = 1
        
        for i in range(128):
            # cv.putText(new_img,string[0+increment:144+increment],(2,7*(y_increment+5)),cv.FONT_HERSHEY_COMPLEX_SMALL,0.3,(255,255,255),1)
            draw.text((2,7*(y_increment*2)),string[0+increment:144+increment],(255,255,255),font=monospace)
            increment+=144
            y_increment+=1
        cv.imshow("win",np.array(pil_img))
        cv.waitKey(0)
        cv.imwrite("out.jpg",np.array(pil_img))

Converter()
