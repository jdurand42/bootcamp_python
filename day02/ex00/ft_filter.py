import sys

def ft_filter(f, iter):
	def check(f, iter):
		if callable(f) == False:
			return False
		if hasattr(iter, '__iter__') == False:
			return False
		return True

	new_iter  =  []
	if check(f, iter) == False:
		return None
	for ele in iter:
		if f(ele) == True:
			new_iter.append(ele)
	return new_iter

print(ft_filter(lambda x: x == 1, [1, 0, 0, 1, 5]))
print(ft_filter(lambda x: x == 'a', ['a', 'a', 0, 'b', 5]))
print(ft_filter(lambda x: x != "casablanca", ["casablanca", 0, "casablanca", 1, 5]))
print(ft_filter(lambda x: x == 18, [1, 0, 0, 1, 5]))
print(ft_filter(lambda x: x == 18, [1, 0, 0, 1, 5]))
#for words in filter(lambda x: x == "casablanca", ["casablanca", 0, "casablanca", 1, 5]):
#	print(words)
for words in ft_filter(lambda x: x == "casablanca", ["casablanca", 0, "casablanca", 1, 5]):
	print(words)
