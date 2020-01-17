from FileLoader import FileLoader
import pandas

def HowManyMedals(df, name):
#	by_sport = df.loc[(df['Year']==year) & (df['Sex']==gender) & (df['Sport']==sport)]
	dic = {}
	by_name = df.loc[df['Name']==name]
	for index, row in by_name.iterrows():
		if row['Year'] not in dic:
			dic[row['Year']] = {}
			dic[row['Year']].update({'G' : 0, 'S' : 0, 'B' : 0})
			if type(row['Medal']) != float:
				dic[row['Year']][str(row['Medal'][0])] += 1
		#	print(dic[row['Year']])
		else:
			if type(row['Medal']) != float:
				dic[row['Year']][str(row['Medal'][0])] += 1
			#	print(dic)
	#	print(dic)
	return dic

file = FileLoader()
df = file.load("athlete_events.csv", ',')
dic = HowManyMedals(df, "Kjetil Andr Aamodt")
print(dic)
