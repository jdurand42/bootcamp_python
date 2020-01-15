import sys

def what_are_the_vars(*args, **kwargs):
	"""Yeah kwargs"""
	var_id = 0
	obj = ObjectC
	for arg in args:
		setattr(obj, "var_" + str(var_id), arg)
		var_id += 1
	for kwarg in kwargs:
		if "var_" in kwarg:
			return None
	for kwarg in kwargs.values():
		setattr(obj, "var_" + str(var_id), kwarg)
		var_id += 1
	while getattr(obj, "var_" + str(var_id), False) != False:
		delattr(obj, "var_" + str(var_id))
		var_id += 1
	return obj

class ObjectC(object):
	#var_id = 0
	def __init__(self):
		pass

def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")

if __name__ == "__main__":
	obj = what_are_the_vars(7, 8, 9)
	doom_printer(obj)
	obj = what_are_the_vars("ft_lol", "Hi")
	doom_printer(obj)
	obj = what_are_the_vars()
	doom_printer(obj)
	obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
	doom_printer(obj)
	obj = what_are_the_vars(42, a=10, var_0="world")
	doom_printer(obj)
