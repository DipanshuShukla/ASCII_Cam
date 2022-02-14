from ASCII_Cam import *
import cv2, sys, os
from time import sleep



if __name__ == "__main__":
    obj = ASCII_Cam()

    vidCap = cv2.VideoCapture(0)
    sleep(2)

    while True:
        shape = os.get_terminal_size()
        obj.setShape(shape)

        ret, img = vidCap.read()

        result = obj.ImgToASCII(img)


        print(result, end="\r")
        sys.stdout.flush()

        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
  
    # After the loop release the cap object
    vidCap.release()