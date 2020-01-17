
import pandas
from FileLoader import FileLoader


def youngestFellah(df, year):
	#print(df[['Year', 'Age', 'Sex']])
	dict = {}
	youngest_male = df.loc[(df['Year']==year) & (df['Sex']=="M")].sort_values(by='Age').head(1)
	youngest_female = df.loc[(df['Year']==year) & (df['Sex']=="F")].sort_values(by='Age').head(1)
	dict['M'] = youngest_male.iloc[0, 3]
	dict['F'] = youngest_female.iloc[0, 3]
	return dict


file = FileLoader()
df = file.load("athlete_events.csv", ',')
year_1992 = youngestFellah(df, 1992)
print(year_1992)
