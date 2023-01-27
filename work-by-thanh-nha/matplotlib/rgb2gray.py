'''
StackOverFlow:
https://stackoverflow.com/questions/12201577/how-can-i-convert-an-rgb-image-into-grayscale-in-python

How can I convert an RGB image into grayscale in Python?
'''
#---------Generic Code Example---------------------------------
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
img = mpimg.imread("C:\\Users\\tumit\\Downloads\\apple.jpg") #Random test file
plt.imshow(img)
#plt.show()
#--------------------------------------------------------------

#covert to grayscale <= Natural Language Prompt For Copilot
gray = img.mean(axis=2)
plt.imshow(gray, cmap='gray')
plt.show()


'''
StackOverFlow: Best Answer to the question for comparison
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

img = mpimg.imread("C:\\Users\\tumit\\Downloads\\apple.jpg")     
gray = rgb2gray(img)    
plt.imshow(gray, cmap=plt.get_cmap('gray'))
plt.show()
'''
