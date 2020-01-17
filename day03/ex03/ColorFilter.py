
import numpy as np
from ImageProcessor import ImageProcessor

class ColorFilter():
	def __init(self):
		pass
	def invert(self, array):
		#def sub_rgb(n):
		#	return 1 - n
		#return np.apply_along_axis(sub_rgb, 2, array)
		return 1 - array

	def to_blue(self, array):
		filtered = np.zeros(array.shape)
		filtered[: , : ,2] = array[: , : ,2]
		return filtered

	def to_green(self, array):
	#	filtered = array
	#	for y in filtered:
	#		for x in y:
				#x[1] = 1
	#			x[0] = 0
	#			x[2] = 0
		filtered = self.to_blue(array) - self.to_blue(array)
		filtered[: , : ,1] = array[: , : ,1]
		return filtered

	def to_red(self, array):
#		filtered = array
#		for y in filtered:
#			for x in y:
#				#x[0] = 1
#				x[1] = 0
#				x[2] = 0
#		return filtered
		filtered = self.to_blue(array) - self.to_blue(array)
		filtered[: , : ,0] = array[: , : ,0]
		return filtered

	def celluloid(self, array, treshold = 45):
		def lining(n):
			return np.linspace(0, n, 70)[treshold]
		return np.apply_along_axis(lining, 2, array)

	def bright(self, array, threshold = 20):
	#	def lining(n):
	#		return np.linspace(n, 1, 70)[treshold]
		return np.linspace(array, 1, 70)[threshold]
	#	filtered = array
	#	for y in filtered:
	#		for x in y:
	#			for bit in x:
	#				bit = 1
	#				print(bit)
	#	return filtered



img = ImageProcessor()
tab = img.load("42AI.png")
color = ColorFilter()
#img.display(tab)
img.display(color.invert(tab))
img.display(color.to_blue(tab))
img.display(color.to_green(tab))
img.display(color.to_red(tab))
#print(np.linspace(0.5, 0, 15))
cell = color.celluloid(tab)
img.display(cell)

"""
	Ni, Nk = a.shape[:axis], a.shape[axis+1:]
for ii in ndindex(Ni):
    for kk in ndindex(Nk):
        f = func1d(arr[ii + s_[:,] + kk])
        Nj = f.shape
        for jj in ndindex(Nj):
            out[ii + jj + kk] = f[jj]
"""
