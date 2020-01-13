# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdurand <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/01/13 20:57:12 by jdurand           #+#    #+#              #
#    Updated: 2020/01/13 21:17:18 by jdurand          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
#erreur sur nombres negatifs mais osef la flemme
ac = len(sys.argv)
if ac < 3 or ac > 3:
	print("Error")
	sys.exit()
code = sys.argv[1]
if code.isdigit():
	print("Error")
	sys.exit()
code = sys.argv[2]
if not code.isdigit():
	print("Error")
	sys.exit()
n = int(sys.argv[2])
stack = sys.argv[1].split()
stack2 = []
for s in stack:
	if len(s) > n:
		stack2.append(s)
# print(stack)
print(stack2)	
