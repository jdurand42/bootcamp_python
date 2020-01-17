
import pandas
import numpy as np

class FileLoader():
	def __init__(self):
		pass

	def load(self, path, sep = ','):
		df = pandas.read_table(path, sep)
		print("DataSet format :" + str(df.shape[0]) + " x " + str(df.shape[1]))
		return df

	def display(self, df, n):
		if n > 0:
			print(df.head(n))
		elif n < 0:
			print(df.tail(abs(n)))

fl = FileLoader()
df = fl.load("athlete_events.csv", ",")
fl.display(df, 12)
