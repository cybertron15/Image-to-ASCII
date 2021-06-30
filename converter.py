import cv2 as cv

class Converter():
    def __init__(self):
        path = r"Image-to-ASCII\images\swadha2.jpg"
        self.reading_img(path)
    
    def reading_img(self,path):
        img = cv.imread(path)
        height, width = img.shape[0],img.shape[1]
        print(img.shape)
        self.resizing(img,height,width)
    
    def resizing(self,img,height,width):
        img = cv.resize(img,(int(width*0.10),int(height*0.10)),interpolation=cv.INTER_AREA)
        resized_height, resized_width = img.shape[0],img.shape[1]
        print(img.shape)
        self.grayscaling(img,resized_height,resized_width)
    
    def grayscaling(self,img,height,width):

        grayed_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        self.converting_to_ascii(grayed_img,height,width)
    
    def converting_to_ascii(self, grayed_img,height,width):

        ascii = ['@#','#S','S%','%?','??',"**",";;",":-","-.","..",".."]
        string = ""
        for i in range(height):
            for j in range(width):
                string += ascii[-(grayed_img[i][j])//25] + ""
            string+="\n"
        self.writing_to_file(string)
    
    def writing_to_file(self,string):

        with open("Image-to-ASCII\\text.txt","w") as file:
            file.write(string)
        print("done")

Converter()
