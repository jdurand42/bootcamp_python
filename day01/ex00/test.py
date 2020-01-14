# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdurand <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/14 12:57:50 by jdurand           #+#    #+#              #
#    Updated: 2020/01/14 19:19:39 by jdurand          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import datetime
from recipe import Recipe
from book import Book



# it's all working but i don't have the check in add_recipe because of the same name


kebab = Recipe(1)
kebab2 = Recipe(1)
kebab3 = Recipe(2)
kebab4 = Recipe(3)
cookbook = Book()
print(cookbook.creation_date)
print(kebab.recipe_type)
print(kebab2.recipe_type)
print(kebab3.recipe_type)
print(kebab4.recipe_type)

print("-------Book creation-------")
cookbook.add_recipe(kebab)
cookbook.add_recipe(kebab2)
cookbook.add_recipe(kebab3)
cookbook.add_recipe(kebab4)

cookbook.get_recipes_by_types('lunch')
cookbook.get_recipes_by_types('dessert')
#print(type(recipe))
#cookbook.add_recipe(12)
print("-------TEST ON TIME AND SEARCHES--------")
cookbook.get_recipe_by_name('kebab')
cookbook.print_times()
generic = Recipe()
cookbook.add_recipe(generic)
cookbook.get_recipe_by_name(generic.name)
cookbook.print_times()
cookbook.get_recipes_by_types(generic.recipe_type)

