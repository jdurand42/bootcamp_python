
def log(func):
	def start(*args):
		print("start")
		func(*args)
		print("end")
	return start

@log
def test(*args):
	for arg in args:
		print(arg)

#lol = log(test)
#lol()
test(1, 2, 3)
