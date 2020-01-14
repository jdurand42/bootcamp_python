# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    eval.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdurand <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/14 20:36:15 by jdurand           #+#    #+#              #
#    Updated: 2020/01/14 21:25:59 by jdurand          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def check_stuff(coefs, words):
	for el in coefs:
		if isinstance(el, float) == False and isinstance(el, int) == False:
			print("Error there")
			return 0
	for el in words:
		if isinstance(el, str) == False:
			print("Error here")
			return 0
	return 1
		

class Evaluator:
	def zip_evaluate(coefs, words):
		if isinstance(coefs, list) == False or isinstance(words, list) == False:
			return
		if len(words) != len(coefs):
			print(-1)
		if check_stuff(coefs, words) == 0:
			return
		res = 0
		for coef, word in zip(coefs, words):
			res += coef * len(word)
		print(res)

	def enumerate_evaluate(coefs, words):
		if isinstance(coefs, list) == False or isinstance(words, list) == False:
			return
		if len(words) != len(coefs):
			print(-1)
		if check_stuff(coefs, words) == 0:
			return
		res = 0
		for word in enumerate(words):
			res += len(word[1]) * coefs[word[0]]
		print(res)
		
words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
Evaluator.zip_evaluate(coefs, words)
Evaluator.enumerate_evaluate(coefs, words)	
