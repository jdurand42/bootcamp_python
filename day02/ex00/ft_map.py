import sys

def ft_map(f, iter):
	def check(f, iter):
		if callable(f) == False:
			return False
		if hasattr(iter, '__iter__') == False:
			return False
		return True

	if check(f, iter) == False:
		return None
	new_lst = []
	for ele in iter:
		new_lst.append(f(ele))
	return new_lst

def double(n):
	return n + n

print(ft_map(double, [0, 1, 2, 3, 4]))
print(ft_map(lambda x: x * x, [0, 1, 2, 3, 4]))
print(ft_map(double, "dasdasd"))
print(ft_map(5, [0, 1, 2, 3, 4]))
print(ft_map(lambda x: x * x, 5))
