# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdurand <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/14 11:52:50 by jdurand           #+#    #+#              #
#    Updated: 2020/01/14 12:57:10 by jdurand          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

class enter_recipe:
	def get_lvl(inp):
		if inp.isdigit() == True:
			if 0 < int(inp) < 6:
				return int(inp)
		return 0
	def get_int(inp):
		if inp.isdigit() == True:
			return int(inp)
		else:
			return 0
	def check_validity(recipe):
		if recipe.name == "" or recipe.cooking_lvl == 0 or recipe.cooking_time == 0 or len(recipe.ingredients) == 0 or recipe.recipe_type == "":
			print("Error, the recipe is not valid, aborting")
			sys.exit()

class recipe:
	"""A recipe"""
	name = ""
	cooking_lvl = 0
	cooking_time = 0
	ingredients = []
	description = ""
	recipe_type = ""

	def __init__(self, param = 0):
		if param == 0:
			self.name = input("name: \n")
			self.cooking_lvl = enter_recipe.get_lvl(input("Level: \n"))
			self.cooking_time = enter_recipe.get_int(input("cooking time: \n")) 
			self.ingredients = input("ingredients: i1 i2 ...\n").split()
			self.description = input("Description (optional): \n")
			self.recipe_type = input("Recipe type: \n")
			enter_recipe.check_validity(self)
		else: #generic generation
			self.name = "kebab"
			self.cooking_lvl = 4
			self.cooking_time = 25
			self.ingredients = ['salade', 'tomate', 'oignons', 'chat']
			self.description = "Don't eat this"
			if param == 1:
				self.recipe_type = "lunch"
			elif param == 2:
				self.recipe_type = "starter"
			else:
				self.recipe_type = "dessert"
			
	def print_recipe(self):
		print(self.name)
		print(self.cooking_lvl)
		print(self.cooking_time)
		print(self.ingredients)
		print(self.description)
		print(self.recipe_type)
	
	def __str__(self):
		"""return the string to print with the recipe info"""
		txt = self.name + ": " + self.description
		return txt

#gen = recipe()
#gen.print_recipe()
#kebab = recipe(1)
#kebab.print_recipe()
#print(str(kebab))

