from FileLoader import FileLoader
import pandas

class SpatioTemporalData():
	def __init__(self, df):
		self.df = df
		pass
	def when(self, location):
		lst = []
		by_location = df.loc[df['City']==location]
		for index, row in by_location.iterrows():
			if row['Year'] not in lst:
				lst.append(row['Year'])
		return lst

	def where(self, year):
		lst = []
		by_location = df.loc[df['Year']==year]
		for index, row in by_location.iterrows():
			if row['City'] not in lst:
				lst.append(row['City'])
		return lst

fl = FileLoader()
df = fl.load("athlete_events.csv", ',')
stp = SpatioTemporalData(df)
print(stp.when('Paris'))
print(stp.where(2004))
