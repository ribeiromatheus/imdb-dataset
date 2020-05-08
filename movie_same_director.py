import pandas as pd
import seaborn as sns

# Movie from the same director

imdb = pd.read_csv('https://raw.githubusercontent.com/ribeiromatheus/imdb-data/master/movies.csv')

sns.set_style('whitegrid')

imdb.sort_values('gross', ascending=False).head()

imdb.drop_duplicates()
imdb_usa = imdb.query('country == "USA"')
imdb_usa.sort_values('budget', ascending=False)

imdb_usa['profit'] = imdb_usa['gross'] - imdb_usa['budget']

budget_gross = imdb_usa.query('budget > 0 | gross > 0')[['title_year', 'profit']].dropna()

movies_by_director = imdb_usa['director_name'].value_counts()
gross_director = imdb_usa[['director_name', 'gross']].set_index('director_name').join(movies_by_director, on='director_name')
gross_director.columns = ['dindin', 'filmes_irmaos']
gross_director = gross_director.reset_index()

gross_director.drop_duplicates('director_name').query('filmes_irmaos == 18')
gross_director[(gross_director['filmes_irmaos'] > 16) & (gross_director['filmes_irmaos'] < 20)]

plt.figure(figsize=(12, 6))
sns.scatterplot(x="filmes_irmaos", y="dindin", data=gross_director)