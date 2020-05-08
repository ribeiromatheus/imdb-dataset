import pandas as pd
import seaborn as sns

# IMDB - profit and budget

imdb = pd.read_csv('https://raw.githubusercontent.com/ribeiromatheus/imdb-data/master/movies.csv')

sns.set_style('whitegrid')

imdb.sort_values('gross', ascending=False).head()

imdb.drop_duplicates()
imdb_usa = imdb.query('country == "USA"')
imdb_usa.sort_values('budget', ascending=False)

imdb_usa['profit'] = imdb_usa['gross'] - imdb_usa['budget']

budget_gross=  imdb_usa.query('budget > 0 | gross > 0')[['budget', 'profit']].dropna()

sns.scatterplot(x='budget', y='profit', data=budget_gross)