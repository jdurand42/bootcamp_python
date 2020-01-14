# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdurand <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/14 11:48:49 by jdurand           #+#    #+#              #
#    Updated: 2020/01/14 16:12:11 by jdurand          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from recipe import recipe
import sys
import datetime

def	check_if_name(recipes_list, name):
	for recipe in recipes_list:
		if name == recipe.name:
			recipe.print_recipe()

class book:
	name = ""
	creation_date = datetime.datetime.now()
	last_update = datetime.datetime.now()
	recipes_list = {'starter': [],
			'lunch': [],
			'dessert': [],
			'unknown': []}
	def __init__(self):
		pass
	def add_recipe(self, recipe):
		#if str(type(b)) != str(type(recipe)):
		#	print("Not right object")
		#	sys.exit()
		if recipe.recipe_type in self.recipes_list:
			self.recipes_list[recipe.recipe_type].append(recipe)
		else:
			self.recipes_list['unknown'].append(recipe)
		self.last_update = datetime.datetime.now()

	def get_recipes_by_types(self, recipe_type):
		if recipe_type in self.recipes_list:
			for recipe in self.recipes_list[recipe_type]:
				recipe.print_recipe()
		else:
			print("recipe_type unknown")

	def get_recipe_by_name(self, name):
		check_if_name(self.recipes_list['starter'], name)
		check_if_name(self.recipes_list['lunch'], name)
		check_if_name(self.recipes_list['dessert'], name)
		check_if_name(self.recipes_list['unknown'], name)

	def print_times(self):
		print("Book created in: " + str(self.creation_date))
		print("Last updated in: " + str(self.last_update))
	

