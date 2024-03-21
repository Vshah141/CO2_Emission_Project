from sklearn.model_selection import train_test_split
from sklearn import linear_model
import pandas as pd
import numpy as np


def Model_training(data):
    train, test = train_test_split(data, test_size=0.2, random_state=42)
    # print("Train set shape:", train.shape)
    # print("Test set shape:", test.shape)
    # plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='blue')
    # plt.xlabel("Engine size")
    # plt.ylabel("Emission")
    # plt.show()
    regr = linear_model.LinearRegression()
    train_x = np.asanyarray(train[['ENGINESIZE']])
    train_y = np.asanyarray(train[['CO2EMISSIONS']])
    regr.fit(train_x, train_y)
    a = regr.coef_
    b=regr.intercept_
    # print ('Coefficients: ', regr.coef_)
    # print ('Intercept: ',regr.intercept_)
    # plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='blue')
    # plt.plot(train_x, regr.coef_[0][0]*train_x + regr.intercept_[0], '-r')
    # plt.xlabel("Engine size")
    # plt.ylabel("Emission")
    test_x = np.asanyarray(test[['ENGINESIZE']])
    test_y = np.asanyarray(test[['CO2EMISSIONS']])
    test_y_ = regr.predict(test_x)
    return a,b
