# Then we visualize the preprocessed data.
df_color = df1.groupby('color').size()
print(df_color)

df_color.plot.pie(labels=['Black and White', 'Color'])

df_language = df1.groupby('language').size()
print(df_language)

df_color.plot.pie(labels=['Other', 'English'])

plot_facenumber = df3['facenumber_in_poster'].plot.hist(color = 'green', range = (0, 10))

# The relationship between 'gross' and 'imdb_score'
df55 = df5.drop(index = df5.gross[df5.gross == 0].index)
df_imdb = df55.sort_values(by=['imdb_score'])
# print(df55)
plot1 = df_imdb.plot.line(x='gross', y='imdb_score')
# The larger gross, the more likely to have high imdb_scores.

# The relationship between 'facebook_likes' and 'imdb_score'
df6 = df5.drop(index = df5.movie_facebook_likes[df5.movie_facebook_likes == 0].index)
df_facebook_likes = df6.sort_values(by=['imdb_score'])
# print(df6)
plot2 = df_facebook_likes.plot.line(y='movie_facebook_likes', x='imdb_score')
# The more facebook likes, the more likely to have high imdb_scores.

plot3 = df5['imdb_score'].plot.hist(color = 'green')

plot4 = df5['num_critic_for_reviews'].plot.hist(color = 'blue')