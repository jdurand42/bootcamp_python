

import sys
print(sys.argv)

s1 = sys.argv[1]
i = len(s1) - 1
b = ""
b2 = ""
len1 = len(s1)

while i >= 0:
	b = b + s1[i]
	i -= 1
print(b)

i = 0
len2 = len(b)
while i < len2:
	code = ord(b[i])
	if "a" <= b[i] <= "z":
		code = code - 32
	if "A" <=  b[i] <= "Z":
		code = code + 32
	b2 = b2 + chr(code)
	i += 1
print(b2)

