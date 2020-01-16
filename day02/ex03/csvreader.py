
import os.path
from os import path

class Csvreader():
	def __init__(self, name=None, sep=',', header=True, skip_top=0, skip_bottom=0):
		self.sep = sep
		self.header = header
		self.header_id = 0
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom
		self.name = name
		pass

	def __enter__(self):
		if path.exists(self.name) == False:
			print("file does not exists")
			return None
		self.file = open(self.name, 'r')
		return self

	def __exit__(self, file, value, traceback):
		if path.exists(self.name) == True:
			self.file.close()

	def get_data(self):
		tab = []
		#header-ing
		header = self.file.readline().replace('\n', '').split(self.sep)
		if self.header == True:
			tab.append(header)

		# skips and gnl
		for line in self.file.readlines():
			if self.skip_top > 0:
				self.skip_top -= 1
			else:
				line_p = line.replace('\n', '').split(self.sep)
				if len(line_p) > len(header):
					return None
				len_diff = len(header) - len(line_p)
				while len_diff > 0:
					len_diff -= 1
					line_p.append("None")
				tab.append(line_p)
		if self.skip_bottom > 0:
			del tab[len(tab) - self.skip_bottom:]
		return tab

	def get_header(self):
		header = self.file.readline().replace('\n', '').split(self.sep)
		return header
#with Csvreader("RICHARD") as opened:
#	print(opened)
with Csvreader("gooddasdas.csv") as opened:
	print(*opened.get_header())
