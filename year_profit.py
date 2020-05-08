import pandas as pd
import seaborn as sns

# profi according to production year

imdb = pd.read_csv('https://raw.githubusercontent.com/ribeiromatheus/imdb-data/master/movies.csv')

sns.set_style('whitegrid')

imdb.sort_values('gross', ascending=False).head()

imdb.drop_duplicates()
imdb_usa = imdb.query('country == "USA"')
imdb_usa.sort_values('budget', ascending=False)

imdb_usa['profit'] = imdb_usa['gross'] - imdb_usa['budget']

budget_gross = imdb_usa.query('budget > 0 | gross > 0')[['title_year', 'profit']].dropna()

sns.scatterplot(x='title_year', y='profit', data=budget_gross)