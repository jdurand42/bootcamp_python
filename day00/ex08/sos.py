# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    sos.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdurand <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/13 21:17:43 by jdurand           #+#    #+#              #
#    Updated: 2020/01/13 22:00:13 by jdurand          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0': '-----'} # merci a un random sur internet :)

def to_morse(char):
	return MORSE_CODE_DICT[char]

# error si espace mais c'est comme ca dans le sujet lol

ac = len(sys.argv)
if (ac < 2):
	print("Error")
	sys.exit()
i = 1
while i < ac:
	s = sys.argv[i]
#	print(s.isalnum())
	if s.isalnum() == False:
		print("Error")
		sys.exit()
	i += 1
i = 1
while i < ac:
	len_s = len(sys.argv[i])
	j = 0
	s = sys.argv[i].upper()
	for char in s:
		if j < len_s - 1:
			print(to_morse(char), end = " ")
		else:
			print(to_morse(char), end  = "")
		j += 1
	if i < ac - 1:
		print(" /", end = " ")
	else:
		print("")
	i += 1
