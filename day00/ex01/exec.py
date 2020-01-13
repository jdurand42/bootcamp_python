

import sys

argc = len(sys.argv) - 1
while argc > 0: 
	s1 = sys.argv[argc]
	i = len(s1) - 1
	b = ""
	b2 = ""
	len1 = len(s1)

	while i >= 0:
		b = b + s1[i]
		i -= 1
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
	if argc > 1:
		print(b2, end = ' ')
	else:
		print(b2)
	argc -= 1
