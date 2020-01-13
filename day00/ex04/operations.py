# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdurand <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/13 16:20:54 by jdurand           #+#    #+#              #
#    Updated: 2020/01/13 16:43:45 by jdurand          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def error(msg):
	print(msg)
	sys.exit()

def check_number(s):
	first_char = 0
	for el in s:
#		c = ord(el)
		if (el < '0' or el > '9'):
			if first_char != 0:  
				error("InputError: only numbers")
			if first_char and el != "-" and el != "+":
				error("InputError: only numbers")
		first_char = 1

ac = len(sys.argv)
if ac > 3:
	error("InputError: too many arguments")
if ac == 1:
	error("Example operations.py 10 3")
if ac < 3:
	error("InputError: Not enought arguments (2 are needed)")
check_number(sys.argv[1])
check_number(sys.argv[2])
#if here -> av1 and av2 are okay
n1 = int(sys.argv[1])
n2 = int(sys.argv[2])
#print(n1)
#print(n2)

#operations

print("sum:		", n1 + n2)
print("Difference:	", n1 - n2)
print("Product:		", n1 * n2)
print("Quotient:	", end = "")
if n2 == 0:
	print("ERROR (div by zero)")
else:
	print(n1 / n2)
print("Remainder:	", end = "")
if n2 == 0:
	print("ERROR (modulo by zero)")
else:
	print(n1 % n2)

