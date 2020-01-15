import sys

def ft_reduce(f, iter):
	def check(f, iter):
		if callable(f) == False:
			return False
		if hasattr(iter, '__iter__') == False:
			return False
		return True

	# dssdasd
	if check(f, iter) == False:
		return None
	if len(iter) < 2:
		return iter[0]

	res = f(iter[0], iter[1])
	for el in iter[2:]:
		res = f(res, el)
	return res

print(ft_reduce(lambda x, y: x + y, [12]))
print(ft_reduce(lambda x, y: x + y, ["das, "";ddd", "dadd"]))
