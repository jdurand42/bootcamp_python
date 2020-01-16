
import numpy as np
from random import random

class NumPyCreator(object):
	def __init__(self):
		pass
	def from_list(self, lst):
		return np.array(lst)
	def from_tuple(self, tuple):
		return np.array(tuple)
	def from_iterable(self, iter):
		return np.array(iter)
	def from_shape(self, shape_tuple, value = 0):
		return np.full(shape_tuple, value)
	def iddentity(self, n):
		return np.eye(n)
	def random(self, shape):
		return np.random.rand(shape[0], shape[1])


#npc.from_shape(shape)
#print(a)
