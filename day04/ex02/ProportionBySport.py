
import pandas
from FileLoader import FileLoader

#	youngest_male = df.loc[(df['Year']==year) & (df['Sex']=="M")].sort_values(by='Age').head(1)


def porportionBySport(df, year, sport, gender):
#	by_sport = df.loc[(df['Year']==year) & (df['Sex']==gender) & (df['Sport']==sport)]
	all = df.loc[(df['Year']==year) & (df['Sex']==gender)]
	all.drop_duplicates()
	by_sport = all.loc[all['Sport']==sport]
	print(by_sport)
	print(all)
	return  by_sport.shape[0] / all.shape[0]

file = FileLoader()
df = file.load("athlete_events.csv", ',')
print(porportionBySport(df, 1992, "Basketball", "F"))
print(porportionBySport(df, 2000, "Synchronized Swimming", "F"))
