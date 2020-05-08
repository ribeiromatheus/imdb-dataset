import pandas as pd
import seaborn as sns

# Color or Black and White

imdb = pd.read_csv('https://raw.githubusercontent.com/ribeiromatheus/imdb-data/master/movies.csv')

imdb.sort_values('gross', ascending=False).head()

color_or_bw = imdb.query("color in ['Color', ' Black and White']")
color_or_bw["color_0_ou_1"] = (color_or_bw["color"]=="Color") * 1

# sns.scatterplot(data=color_or_bw, x="color_0_ou_1", y="gross")

sns.boxplot(x='color', y='imdb_score', data=color_or_bw)