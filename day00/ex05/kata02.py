# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata02.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdurand <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/13 17:38:25 by jdurand           #+#    #+#              #
#    Updated: 2020/01/13 18:00:21 by jdurand          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


t = (3,30,2019,9,25)

def print_t(n, sep):
	if n < 10:
		print(0, end = "")
		print(str(n), end = sep)
	else:
		print(str(n), end = sep)

print_t(t[3], "/")
print_t(t[4], "/")
print_t(t[2], " ")
print_t(t[0], ":")
print_t(t[1], "\n") 
