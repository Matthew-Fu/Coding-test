# Neural Network
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import sklearn
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPRegressor

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn.metrics import r2_score

print(df5.shape)
print(df5)
df555 = df5
df555.insert(df555.shape[1], 'result', 0)

print(df555.columns.values)

df555.loc[df555.imdb_score>7, 'result']= 1
print(df555)
print(df555.shape)

df555.describe().transpose()

X = df555.drop(['imdb_score', 'result'], axis=1)
y = df555['result']
df555.describe().transpose()

X_train, X_test, y_train, y_test = train_test_split(X, y)
print(X_train.shape)
print(X_test.shape)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
StandardScaler(copy=True, with_mean=True, with_std=True)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.neural_network import MLPClassifier
mlp = MLPClassifier(hidden_layer_sizes=(11,11,11),max_iter=500)
mlp.fit(X_train, y_train)
predictions = mlp.predict(X_test)
from sklearn.metrics import classification_report,confusion_matrix
print(confusion_matrix(y_test,predictions))
print(classification_report(y_test,predictions))

print(len(mlp.coefs_))
print(len(mlp.coefs_[0]))
print(len(mlp.intercepts_[0]))

# The precision, recall and f1-score seem good, Neural Network is a good model for prediction.