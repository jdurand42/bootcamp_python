
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
		return np.full(shape, value)
	def iddentity(self, n):
		return np.eye(n)
	def random(self, shape):
		return np.random.rand(shape[0], shape[1])


npc = NumPyCreator()

print(npc.from_list([[1,2,3],[6,3,4]]))
print(npc.from_tuple(("a", "b", "c")))
print(npc.from_iterable(range(5)))
shape=(3,5)
print(npc.from_shape(shape, 12))
print(npc.iddentity(4))
print(npc.random((3,5)))
#npc.from_shape(shape)
#print(a)
