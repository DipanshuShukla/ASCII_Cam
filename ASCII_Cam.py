from ctypes import resize
import cv2
import numpy as np

charScale ='NÑ@#W$9876543210?!abc;:+=-,._                 '[::-1]
charScale1 = " .:-=+*#%@"

class ASCII_Cam:
    def __init__(self) -> None:
        self.charScale = charScale
        self.height, self.width = 100, 40

    def setShape(self, size: tuple):
        '''
        (height,width)
        '''
        self.height, self.width = size
    
    def ImgToASCII(self,img):
        #resize and grayscale img
        img = cv2.resize(img, dsize=(self.height, self.width), interpolation=cv2.INTER_CUBIC)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        mapToChar = lambda x : self.charScale[(x*len(self.charScale)//256)]
        vmapToChar = np.vectorize(mapToChar)
        return self.PrintableToTerminal(vmapToChar(img))

    def PrintableToTerminal(self, charImg):
        result = []
        for i in charImg:
            for j in i:
                result.append(j)
            result.append("\n")

        return "".join(result)






if __name__ == "__main__":
    obj = ASCII_Cam()

    img = cv2.imread("test_imgs/test0.jpg")

    img = obj.ImgToASCII(img)

    print(img)

