from google.colab import files
uploaded = files.upload()

import pandas as pd
import io
df1 = pd.read_csv(io.BytesIO(uploaded['movie_metadata.csv']))

# print(df1)
# print(type(df1))
# print(df1.columns.values)

# drop 'color', 'language', 'country', 'plot_keywords' columns
df2 = df1.drop(['color', 'language', 'country', 'plot_keywords'], axis = 1)

# print(df2)
# print(df2.columns.values)

# drop 'director_name', 'actor_2_name', 'actor_1_name', 'actor_3_name' columns
df3 = df2.drop(['director_name', 'actor_2_name', 'actor_1_name', 'actor_3_name'], axis = 1)

# Remove the 'movie_imdb_link' and 'movie_title'
df4 = df3.drop(['movie_imdb_link', 'movie_title', 'duration', 'content_rating','facenumber_in_poster', 'title_year', 'genres', 'aspect_ratio'], axis = 1)

# print(df4)
# print(df4.columns.values)

# There are some movies having no budgets or gross, we remove these rows.
df5 = df4.dropna(axis=0, how='any')
# print(df5)
# print(df5.columns.values)