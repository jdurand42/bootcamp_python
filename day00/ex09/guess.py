# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdurand <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/14 11:20:53 by jdurand           #+#    #+#              #
#    Updated: 2020/01/14 11:43:21 by jdurand          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

# randrange(start,stop,step)

def menu():
	print("Guess a number between 1 and 99")

n = random.randrange(1, 99, 1)
print(n)
menu()
n_in = 0
guess = 0
i = 0
while guess != n:
	n_in = input("Go ahead, try to guess\n")
	if  n_in.isdigit() == False:
		guess = 0
		print("Works only with numbers\n")
	else:
		guess = int(n_in)
	if guess != 0:
		if guess < n:
			print("Too low")
		elif guess > n:
			print("too high")
		i += 1
print("Congratulations, you chose wisely !!!!")
print("You won in " + str(i) + " attempt")
print("Champagne !!!!")
	
