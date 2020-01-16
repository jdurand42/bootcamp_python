
#from ImageProcessor import ImageProcessor
import numpy as np
from NumPyCreator import NumPyCreator
from scipy import ndimage
from ImageProcessor import ImageProcessor

def print_np(np):
	for row in np:
		print(np)

class ScrapBooker():
	def __init__(self):
		pass

	def crop(self, array, dimensions, position = (0, 0)):
		if dimensions[0] + position[0] > array.shape[0] or dimensions[1] + position[1] > array.shape[1]:
			print("Error dimension size bigger than img")
			exit()
		return array[position[0]:dimensions[0]+position[0],position[1]:dimensions[1]+position[1]]
		#array.reshape(dimensions)

	def thin(self, array, n, axis):
		return np.delete(array, slice(0, array.shape[axis], n), axis)

	def juxtapose(self, array, n, axis):
		return np.concatenate([array] * n, axis)

	def mosaic(self, array, dimensions):
		return np.concatenate([np.concatenate([array] * dimensions[0], 0)] * dimensions[1], 1)
		#return juxtapose(juxtapose(array, dimensions[0], 0), dimensions[1])


#		print(array)

img = ImageProcessor()
tab = img.load("42AI.png")
#img.display(tab)
#npc = NumPyCreator()
#n = npc.from_shape((15,), 0)
#print_np(n)
scrap = ScrapBooker()

img.display(scrap.crop(tab, (30, 30), (25, 25)))
img.display(scrap.thin(tab, 5, 0))
img.display(scrap.juxtapose(tab, 5, 0))
img.display(scrap.mosaic(tab, (5, 6)))
