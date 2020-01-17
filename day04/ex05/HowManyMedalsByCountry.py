from FileLoader import FileLoader
import pandas


def howManyMedalsByCountry(df, country):
	dic = {}
	dic_years = {}
	by_name = df.loc[df['Team']==country]
	for index, row in by_name.iterrows():
		if row['Year'] not in dic:
			dic[row['Year']] = {}
			dic[row['Year']].update({'G' : 0, 'S' : 0, 'B' : 0})
			if type(row['Medal']) != float:
				if row['Name'] not in dic_years[row['Year']]:
					dic[row['Year']][str(row['Medal'][0])] += 1
					dic_years[row['Year']].append(row['Name'])
			#	print(dic[row['Year']])
		else:
			if type(row['Medal']) != float:
				if row['Name'] not in dic_years[row['Year']]:
					dic[row['Year']][str(row['Medal'][0])] += 1
					dic_years[row['Year']].append(row['Name'])

				#	print(dic)
		#	print(dic)
	return dic


file = FileLoader()
df = file.load("athlete_events.csv", ',')
print(len(howManyMedalsByCountry(df, "France")))
print(len(howManyMedalsByCountry(df, "Belgium")))
print(len(howManyMedalsByCountry(df, "China")))
