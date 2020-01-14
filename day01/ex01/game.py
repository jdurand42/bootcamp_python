# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    game.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdurand <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/14 13:56:09 by jdurand           #+#    #+#              #
#    Updated: 2020/01/14 20:59:37 by jdurand          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


class GotCharacter:
	def __init__(self, first_name, is_alive):
		self.first_name = first_name
		self.is_alive = is_alive

class Stark(GotCharacter):
	def __init__(self, first_name = None, is_alive = True):
		super().__init__(first_name = first_name, is_alive = is_alive)
		self.family_name = "Stark"
		self.family_words = "Winter is Coming"
	def die(self):
		self.is_alive = False
		print("Is " + self.first_name + " alive?")
		print(self.is_alive)
	def print_house_words(self):
		print(self.family_words)

class Niel(GotCharacter):
	def __init__(self, first_name = None, is_alive = True):
		super().__init__(first_name = first_name, is_alive = is_alive)
		self.family_name = "Niel"
		self.family_words = "Le C c'est bien"
	def die(self):
		self.is_alive = False
		print("Is " + self.first_name + " alive?")
		print(self.is_alive)
	def print_house_words(self):
		print(self.family_words)


#arya = Stark("arya")
#arya.die()
#arya.print_house_words()
#xavier = Niel("Xavier")

