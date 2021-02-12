import csv
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

Train_file=open("train.csv")

Test_file=open("test.csv")

train_x=[]
train_y=[]

test_x=[]
test_y=[]

chk=True
for row in Train_file:
    rw=row.split(',')

    if chk:
        chk=False
        continue
    
    x=[]
    y=[]
    x.append(int(rw[0]))
    y.append(float(rw[1]))
    train_x.append(x)
    train_y.append(y)

chk=True

for row in Test_file:
    rw=row.split(',')

    if chk:
        chk=False
        continue
    x=[]
    y=[]
    x.append(int(rw[0]))
    y.append(float(rw[1]))
    test_x.append(x)
    test_y.append(y)

regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(train_x, train_y)

# Make predictions using the testing set
predict_y = regr.predict(test_x)

# The coefficients
print('Coefficients: \n', regr.coef_)
# The mean squared error
print('Mean squared error: %.2f'
      % mean_squared_error(test_y, predict_y))
# The coefficient of determination: 1 is perfect prediction
print('Coefficient of determination: %.2f'
      % r2_score(test_y, predict_y))

ex_x=int(input("Input X-Value:-"))

x_list=[]
x_list.append([ex_x])
# predex_y= (regr.coef_*ex_x) + regr.intercept_

predex_y=regr.predict(x_list)
print("Predicted Value=",predex_y)


# Plot outputs
plt.scatter(test_x, test_y,  color='black')
plt.plot(test_x, predict_y, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()

