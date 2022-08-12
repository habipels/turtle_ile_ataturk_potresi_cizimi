from turtle import shape
from sketchpy import canvas
import cv2
im = cv2.imread('video/att.jpg')
print(im.shape)
obj = canvas.sketch_from_image('video/att.jpg')
obj.draw(threshold =100)