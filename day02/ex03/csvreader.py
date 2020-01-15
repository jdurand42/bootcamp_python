
class Cvsreader():
	def __init__(self, sep=',', header=False, skip_top=0, skip_bottom=0):
		self.sep = sep
		self.header = header
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom
		pass
	def __enter__(self, name):
		file = open(name, 'r')
		print(file.read())
	def __exit__(self, file):
		file.close()



test = Cvsreader()
print(test.header)
test.("fichiernul.txt")
