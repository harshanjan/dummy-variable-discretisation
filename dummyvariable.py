import pandas as pd
import numpy as np
df = pd.read_csv("C:/Users/user/Desktop/DATASETS/animal_category.csv") #loading the datset
df.shape #shape of the data
df.describe() #gives boxplot values 
df = df.drop(['Index'], axis= 1) #removing 1st column as it has nothing to do with modeling
df.columns

#separating variables into 2 by nominal and ordinal data.
x = df.drop(['Types'],axis = 1) #nominal data so we use getdummies
x = pd.get_dummies(x,drop_first = True) #removing first dummy column to avoid dummy variable trap

y = df['Types']
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)
types = pd.DataFrame(y)

df_new = pd.concat([x,types],axis =1)
df_new
