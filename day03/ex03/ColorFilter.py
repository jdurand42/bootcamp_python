
import numpy as np
from ImageProcessor import ImageProcessor

class ColorFilter():
	def __init(self):
		pass
	def invert(self, array):
		def sub_rgb(n):
			return 1 - n
		return np.apply_along_axis(sub_rgb, 2, array)

	def to_blue(self, array):
		filtered = array
		for y in filtered:
			for x in y:
				x[1] = 0
				#x[2] = 1
				x[0] = 0
		return filtered

	def to_green(self, array):
		filtered = array
		for y in filtered:
			for x in y:
				#x[1] = 1
				x[0] = 0
				x[2] = 0
		return filtered

	def to_red(self, array):
		filtered = array
		for y in filtered:
			for x in y:
				#x[0] = 1
				x[1] = 0
				x[2] = 0
		return filtered

	def celluloid(self, array, treshold = 45):
		def lining(n):
			return np.linspace(0, n, 70)[treshold]
		return np.apply_along_axis(lining, 2, array)

	def bright(self, array, treshold = 20):
		def lining(n):
			return np.linspace(n, 1, 70)[treshold]
		return np.apply_along_axis(lining, 2, array)
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
#img.display(color.invert(tab))
#img.display(color.to_blue(tab))
#img.display(color.to_green(tab))
#img.display(color.to_red(tab))
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
