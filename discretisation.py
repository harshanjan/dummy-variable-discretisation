import pandas as pd
import numpy as np
df = pd.read_csv("C:/Users/user/Desktop/DATASETS/iris.csv",encoding = 'unicode_escape')
df.shape
df.describe()
df.columns
df.dtypes
df = df.drop(['Unnamed: 0'], axis= 1) #removing 1st column as it has nothing to do with modeling
x = df.drop(['Species'],axis = 1)
y = df['Species']
x.round(0) #rounded off [continuous data to discrete data]
x = x.astype('int64') #coverting from float to int
x.dtypes

y = pd.get_dummies(y) #creating dummy columns for categorical variable

result = pd.concat((x,y), axis = 1) #combining two dataframes as one
result.dtypes
