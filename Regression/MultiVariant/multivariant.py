import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import *
 
data=pd.read_csv('kc_house_data.csv')
"""pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)"""
print(data.head())
data.columns
data.shape

#independent variable
x=data[['bedrooms','bathrooms','sqft_living','sqft_lot', 'sqft_above', 'sqft_basement','sqft_living15', 'sqft_lot15']]

#dependent variable
y=data.loc[:,'price']

#split train - test data
train_x,test_x,train_y,test_y=model_selection.train_test_split(x,y,train_size=0.8,random_state=1)

#train model
regr=linear_model.LinearRegression()
regr.fit(train_x,train_y)


pred_y=regr.predict(test_x)

#mse r2score
mse=metrics.mean_squared_error(test_y,pred_y)
rscore=metrics.r2_score(test_y,pred_y)
print('Mean Square Error: {}\n Correlation score: {}'.format(mse,rscore) )



# graphs
plt.scatter(test_x['bathrooms'],test_y,color='orange')
plt.scatter(test_x['bathrooms'],pred_y,color='blue')
plt.xticks(())
plt.yticks(())
plt.show()



