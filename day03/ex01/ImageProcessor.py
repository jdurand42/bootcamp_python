
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import os.path
from os import path

class ImageProcessor(object):
	def __init__(self):
		pass
	def load(self, path_img):
		if path.exists(path_img) == False:
			return None
		img = mpimg.imread(path_img)
		print("Resolution: " + str(img.shape[0]) + " x " + str(img.shape[1]))
		return img
		
	def display(self, array):
		plt.imshow(array)
		plt.show()

img = ImageProcessor()
img.display(img.load("42AI.png"))
