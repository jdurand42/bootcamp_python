import sys

def error():
	print("ERROR")
	sys.exit()

ac = len(sys.argv)
if ac > 2:
	error()
if ac == 1:
	sys.exit()
first_char = 0
for el in sys.argv[1]:
#	c = ord(el)
	if (el < '0' or el > '9'):
		if first_char != 0:  
			error()
		if first_char and el != "-" and el != "+":
			error()
	first_char = 1
n = int(sys.argv[1])
print(n)
if n == 0:
	print("I'm Zero.")
elif (n % 2 == 0):
	print("I'm Even.")
else:
	print("I'm Odd.")
