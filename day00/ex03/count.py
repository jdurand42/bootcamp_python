# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdurand <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/13 14:47:34 by jdurand           #+#    #+#              #
#    Updated: 2020/01/13 16:12:57 by jdurand          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def text_analyzer(arg = ""):
	"""
		Count numbers of characters in a text.
	"""
	if len(arg) == 0: #no arguments given
		print("Please write a text for me to analyse")
		arg = input()
	upper = 0
	lower = 0
	punct = 0
	space = 0
	punct_s = ",;.:?!()[]{}-*/" + '"' + "'"
	print(punct_s)
	for char in arg:
		code = ord(char) 
		if "a" <= char <= "z":
			lower += 1
		if 'A' <= char <= 'Z':
			upper += 1
		if char == " ":
			space += 1
		if char in punct_s:
			punct += 1
	print("The text contains ", upper + lower + punct + space, "characters:")
	print("- ", upper, " upper letters")
	print("- ", lower, " lower letters")
	print("- ", punct, " punctuation marks")
	print("- ", space, " spaces")

# help(text_analyser)
#print(text_analyser._doc_)
# text_analyser("rrrrrrrrrr          ;;;;;'';;-AAAAAAAAAAAA584784")
		

