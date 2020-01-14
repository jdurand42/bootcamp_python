# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generator.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdurand <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/14 19:22:18 by jdurand           #+#    #+#              #
#    Updated: 2020/01/14 20:12:49 by jdurand          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

 # function prototype
import re
import random

def shuffle(lst):
	range_max = len(lst) - 1
	while range_max >= 0:
		rand = random.randint(0, range_max)
		b = lst[range_max]
		lst[range_max] = lst[rand]
		lst[rand] = b
		range_max -= 1
		return lst

def generator(text, sep=" ", option=None):
	'''Option is an optional arg, sep is mandatory'''
	if isinstance(text, str) == False:
		print("Error")
		exit()
	if option != None and option != "shuffle" and option != "ordered" and option != "unique":
		print("Error here")
		exit()
	for char in sep:
		s = text.replace(char, sep[0])
	lst = s.split(sep[0])
	print(lst)
	if option == "shuffle":
		lst = shuffle(lst)
	if option == "ordered":
		lst.sort()
		
	i = 0
	while i < len(lst):
		yield lst[i]
		i += 1

for word in generator("111 ;222 ;333; 444; 5 ;6", ";. ", "ordered"):
	print(word)
