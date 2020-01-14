# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdurand <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/13 18:34:19 by jdurand           #+#    #+#              #
#    Updated: 2020/01/14 11:34:18 by jdurand          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

cookbook = {	'sandwich' : {	'ingredients' : ["ham", "bread", "cheese", "tomatoes"],
				'meal' : 'lunch',
				'prep_time' : "10"},
		'cake' : {	'ingredients' : ['flour', 'sugar', 'eggs'],
				'meal' : "dessert",
				'prep_time' : "60"},
		'salad' : {	'ingredients' : ['avocado', 'arugula', 'tomatoes', 'spinach'],
				'meal' : "lunch",
				'prep_time' : "15"}
	}

def print_cookbook():
	n = 1
	for key in cookbook:
		print("recipe number " + str(n), end = " ")
		print(key)
		n += 1 
	
def print_value():
	for key in cookbook:
		for value in cookbook[key]:
			print(value)

def print_items():
	for key in cookbook:
		for value in cookbook[key]:
			for item in cookbook[key][value]:
				print(item)
	
#print_name()
#print_value()
#print_items()

def print_recipe(recipe):
#	checking if recipe exist
#	flag = 0
#	for key in cookbook:
#		if key == recipe:
#			flag = 1
#	if flag == 0:
	if recipe not in cookbook or len(recipe) == 0:
		print("The recipe: " + recipe + " doesn't exist" + '\n')
		return 			
	print("Recipe for " + recipe)
	print("ingredients list: ", end  = "")
	print(cookbook[recipe]['ingredients'])
	print("To be eaten for " + cookbook[recipe]['meal'])
	print("Takes " + cookbook[recipe]['prep_time'] + " minutes of cooking." + "\n")

def del_recipe(recipe):
	if recipe not in cookbook:
		print("The recipe: " + recipe + " doesn't exist" + '\n')
		return
	del(cookbook[recipe])
	print("Recipe successfully deleted : " + recipe + '\n')

def add_recipe(name = "", ingredients = [], meal = "", prep_time = ""):
	if len(name) == 0 or len(ingredients) == 0 or len(meal) == 0 or len(prep_time) == 0:
		print("Recipe not correctly formated :\nadd_recipe('name', ('ing1', 'ing2', ect ..'), 'meal', 'time'\n")
		return
	cookbook[name] = {	'ingredients' : ingredients,
				'meal' : meal,
				'prep_time' : prep_time}

def print_menu():
	print("Select an option")
	print("1: Add a recipe\n2: Delete a recipe\n3: Print a recipe\n4: Print the cookbook\n5: Quit")

def input_ing():
	ingredient_s = input()
	return ingredient_s.split()

#print_menu()
choice = "0"
while choice != "5":
	print_menu()
	choice = input()
	print("\n")
	if choice == "1":
		print("Enter name: ", end = "")
		name = input()
		print("Enter ingredients ", end = "")
		ingredients = input_ing()
		print("Enter meal: ", end = "")
		meal = input()
		print("Enter prep time: ", end = "")
		prep_time = input()
		add_recipe(name, ingredients, meal, prep_time)
		print_recipe(name)
	elif choice == "2":
		print("Enter the recipe you want to delete: ")
		name = input("")
		del_recipe(name)
	elif choice == "3":
		print("Enter the recipe you want to print: ")
		name = input("")
		print_recipe(name)
	elif choice == "4":
		print_cookbook()
	elif choice == "5":
		print("Cookbook closed")
	else:
		print("Choose again, it's incorrect")
	print("\n")
#print(cookbook['sandwich']['prep_time'])

# test lines				
#print_recipe('sandwich')
#print_recipe('henri')
#del_recipe('henri')
#del_recipe('sandwich')
#print_recipe('sandwich')
#add_recipe("kebab", ('dinde', 'chat', 'castor', 'sauce du chef'), "everytime", "25")
#print_recipe("kebab")
#add_recipe()
#print_cookbook()


	
