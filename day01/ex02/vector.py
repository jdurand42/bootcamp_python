# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdurand <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/14 18:34:54 by jdurand           #+#    #+#              #
#    Updated: 2020/01/14 19:21:55 by jdurand          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdurand <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/14 14:38:40 by jdurand           #+#    #+#              #
#    Updated: 2020/01/14 18:32:54 by jdurand          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def error(msg):
	print(msg)
	sys.exit()

def opp(vector_, other, code = 0):
	if isinstance(other, float) == False and isinstance(other, int) == False:
		error("Can't only add floats and ints")
	new_vec_list = []
	i = 0
	while i < vector_.size:
		if code == 0:
			new_vec_list.append(vector_.values[i] + other)
		elif code == 1:
			new_vec_list.append(vector_.values[i] - other)
		elif code == 2:
			new_vec_list.append(vector_.values[i] / other)
		elif code == 3:
			new_vec_list.append(vector_.values[i] * other)
		i += 1	
	i += 1
	new_vec = Vector(new_vec_list)
	return new_vec

class Vector:
	#values
	#size
	"""
		A vector class that support basic mathematic
		La flemme de faire les scalaires maintenant
	"""

	def __init__(self, vec_list):
		self.values = []
		if isinstance(vec_list, list) == True:
			i = 0
			while i < len(vec_list):
				if isinstance(vec_list[i], float) == False:
					error("One of the param of the list isn't a float")
				i += 1 
			self.values = vec_list
			self.size = len(vec_list)
			if self.size < 2:
				error("Error: Size < 1")
#		Init with size
		elif isinstance(vec_list, int) and int(vec_list) > 1:
			n = 0.0
			i = 0
			while i < vec_list:
				self.values.append(n)
				i += 1
				n += 1.0
			self.size = vec_list

#		Init with range
		elif isinstance(vec_list, tuple):
			if len(vec_list) == 2 and isinstance(vec_list[0], int) == True and isinstance(vec_list[1], int) == True:
		#		print(self.values)
				size = vec_list[1] - vec_list[0]
				i = 0
				inc = 1
		#		print(size)
		#		print(vec_list[0])
				if size < 0:
					size = -size
					inc = -1
				if size == 0:
					error("size == 0")
				n = float(vec_list[0])
				while i < size:
					self.values.append(n)
		#			print(n)
					n += inc
					i += 1
				self.size = len(self.values)
			else:
				error("No no no")	
		else:
			error("Not quite right: give vector([float, float, ...]) or vector(size) or vector((int, int))")		
	def print_vector(self, name = "No name"):
		print(name, end = ": ")
		print(self.values)
		print("Size : " + str(self.size))

	def __str__(self):
		return str(self.values) + " || size = " + str(self.size)
	
	def __rpr__(self):
		return "Like str, but now it's official"

	def __add__(self, other):
		return opp(self, other, 0) 
	
	def __sub__(self, other):
		return opp(self, other, 1)

	def __truediv__(self, other):
		if isinstance(other, float) == False and isinstance(other, int) == False:
			error("Can only work with floats and ints")
		if other == 0:
			error("Division by zero")
		return opp(self, other, 2)
	def __mul__(self, other):
		return opp(self, other, 3)	
