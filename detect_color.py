# import the necessary packages
import numpy as np
import argparse
import sys
sys.path.append('C:\Users\Carolyn\Documents\opencv\opencv\sources\modules\python\src2')
import cv2

 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "cheer1.jpg")
args = vars(ap.parse_args())

# load the image
image = cv2.imread("goldfish.jpg")

# define the list of boundaries
#boundaries = [
	#([0, 69, 250], [10, 165, 260 ])#orange
	
#]
lowera=[0, 50, 180]
uppera= [50, 190, 255]
i=0
# loop over the boundaries
	# create NumPy arrays from the boundaries
lower = np.array(lowera, dtype=np.uint8)
upper = np.array(uppera, dtype=np.uint8)
 
	# find the colors within the specified boundaries and apply
	# the mask
mask = cv2.inRange(image, lower, upper)
output = cv2.bitwise_and(image, image, mask = mask)
	# show the images
cv2.imshow("images", output)

cv2.waitKey(0)
flag=0
from PIL import Image
im = output #Can be many different formats.
w= im.size #Get the width and hight of the image for iterating over
#pray = im.tolist()

#for i in range (w):
#        if (im(i)==0):
#                flag=flag
#        else:
#                flag=flag+1
#print "flag"
#print flag
