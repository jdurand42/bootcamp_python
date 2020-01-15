# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generator.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdurand <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/14 19:22:18 by jdurand           #+#    #+#              #
#    Updated: 2020/01/14 20:31:50 by jdurand          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

 # function prototype
import re
import datetime

def shuffle(lst):
	range_max = len(lst) - 1
	while range_max > 0:
		seed = int(str(datetime.datetime.now())[20:25])
		rand = (seed + 0) % range_max
		print(rand)
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
	i = 0
	while i < len(lst):
		if lst[i] == "":
			lst.pop(i)
		i += 1
	print(lst)
	if option == "shuffle":
		lst = shuffle(lst)
	if option == "ordered":
		lst.sort()
	if option == "unique":
		lst = set(lst)

	for el in lst:
		yield el

lst = [0, 1, 1, 5]
lst = set(lst)
print(lst)
#s = str(datetime.datetime.now())
#print(int(s[20:25]))
#print(datetime.datetime.now())
#print((int(str(datetime.datetime.now())[20:25]) + 0) % 50)
#for word in generator("111 ;222 ;333; 444; 5 ;6 dlahsd [asdha has;dh asdh assdhaspod hqwoehqwiihdask ;adsh;akskdh  hhdqwhd adk dqw; dqw]", ";. ", "shuffle"):
for word in generator("richard richard henri pascal henir", " ", "unique"):
	print(word)
#	pass
