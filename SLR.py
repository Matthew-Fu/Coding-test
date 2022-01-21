# Simple Linear Regression 'facebook_likes' and 'imdb_score'
import numpy as np
import matplotlib.pyplot as plt  
import pandas as pd
from sklearn.linear_model import LinearRegression

X = df5.iloc[:, 11].values.reshape(-1, 1)  
Y = df5.iloc[:, 10].values.reshape(-1, 1)  
linear_regressor = LinearRegression() 
linear_regressor.fit(X, Y) 
Y_pred = linear_regressor.predict(X) 
plt.scatter(X, Y)
plt.plot(X, Y_pred, color='red')
plt.title('facebook_likes vs. imdb_score')
plt.xlabel('facebook_likes')
plt.ylabel('imdb_score')
plt.show()