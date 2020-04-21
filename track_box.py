# Python program for Detection of a  
# specific color(blue here) using OpenCV with Python 
import cv2 
import numpy as np


kernel = np.ones((8 ,8), np.uint8)

# Webcamera no 0 is used to capture the frames 
cap = cv2.VideoCapture(0)  
  
# This drives the program into an infinite loop. 
while(1):        
    # Captures the live stream frame-by-frame 
    _, frame = cap.read()  
    # Converts images from BGR to HSV 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([110,50,50]) 
    upper_red = np.array([130,255,255]) 

    lower_blue = np.array([100,150,0])
    upper_blue = np.array([140,255,255])
  
# Here we are defining range of bluecolor in HSV 
# This creates a mask of blue coloured  
# objects found in the frame. 
    mask = cv2.inRange(hsv, lower_blue, upper_blue) 
  
# The bitwise and of the frame and mask is done so  
# that only the blue coloured objects are highlighted  
# and stored in res

    res = cv2.bitwise_and(frame,frame, mask= mask) 



    cv2.imshow('mask',mask) 
    cv2.imshow('res',res)

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    x, y, w, h = cv2.boundingRect(opening)
    print(x, ",",y)

    cv2.circle(frame, (int(x+w/2), int(y+w/2)), 25, (255, 0, 0), 3)
    
    #cv2.imshow('box', res)

    cv2.imshow('frame',frame) 
  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# Destroys all of the HighGUI windows. 
cv2.destroyAllWindows() 
  
# release the captured frame 
cap.release() 
