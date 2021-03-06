# -*- coding: utf-8 -*-
"""ML_Week6

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XuKLhW9LwxkY0sdx0i2jVikh-NlPHqk0
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as pp
# %matplotlib inline
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.model_selection import KFold 
from mpl_toolkits.mplot3d import Axes3D
from sklearn.metrics import mean_squared_error 
from pandas import DataFrame
from matplotlib import pyplot
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn import metrics, svm
import seaborn as sn
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import roc_curve
from sklearn.model_selection import cross_val_score
from sklearn.metrics import auc
from sklearn.linear_model import Ridge
from sklearn.kernel_ridge import KernelRidge

import numpy as np
import pandas as pd
X = [-1, 0, 1]
y = [0, 1, 0]
X = np.array(X).reshape(-1, 1)
y = np.array(y).reshape(-1, 1)
Xtest=np.linspace(-3,3,num=1000).reshape(-1, 1)
print("X:",X)
print("y",y)

import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (12.0, 9.0)
plt.scatter(X, y)
plt.xlabel('Target')
plt.ylabel('Value')
plt.show()

def gaussian_kerne0(distances):
  weights = np.exp(-(0 * (distances ** 2)))
  return weights/np.sum(weights)
def gaussian_kernel(distances):
  weights = np.exp(-(1 * (distances ** 2)))
  return weights/np.sum(weights)
def gaussian_kerne5(distances):
  weights = np.exp(-(5 * (distances ** 2)))
  return weights/np.sum(weights)
def gaussian_kerne10(distances):
  weights = np.exp(-(10 * (distances ** 2)))
  return weights/np.sum(weights)
def gaussian_kerne25(distances):
  weights = np.exp(-(25 * (distances ** 2)))
  return weights/np.sum(weights)

model2 = KNeighborsRegressor(n_neighbors=3,weights=gaussian_kerne0).fit(X, y)
ypred2 = model2.predict(Xtest)
model3 = KNeighborsRegressor(n_neighbors=3,weights=gaussian_kernel).fit(X, y)
ypred3 = model3.predict(Xtest)
model4 = KNeighborsRegressor(n_neighbors=3,weights=gaussian_kerne5).fit(X, y)
ypred4 = model4.predict(Xtest)
model5 = KNeighborsRegressor(n_neighbors=3,weights=gaussian_kerne10).fit(X, y)
ypred5 = model5.predict(Xtest)
model6 = KNeighborsRegressor(n_neighbors=3,weights=gaussian_kerne25).fit(X, y)
ypred6 = model6.predict(Xtest)
plt.scatter(X, y, color='red', marker='+')
plt.plot(Xtest, ypred2, color='blue')
plt.plot(Xtest, ypred3, color='orange')
plt.plot(Xtest, ypred4,color='green')
plt.plot(Xtest, ypred5,color='red')
plt.plot(Xtest, ypred6,color='black')
plt.xlabel("input x"); plt.ylabel("output y")
plt.legend(["k=3,sigma=0","k=3,sigma=1","k=3,sigma=5","k=3,sigma=10","k=3,sigma=25","train"])
plt.show()

import numpy as np
from sklearn.kernel_ridge import KernelRidge
gama_range = [0, 1, 5, 10, 25]
for gama in gama_range:
  model = KernelRidge(alpha=1.0/0.1, kernel='rbf', gamma=gama).fit(X, y)
  ypred = model.predict(Xtest)
  model = KernelRidge(alpha=1.0/1, kernel='rbf', gamma=gama).fit(X, y)
  ypred2 = model.predict(Xtest)
  model = KernelRidge(alpha=1.0/1000, kernel='rbf', gamma=gama).fit(X, y)
  ypred3 = model.predict(Xtest)
  import matplotlib.pyplot as plt
  plt.rc('font', size=18); plt.rcParams['figure.constrained_layout.use'] = True
  plt.scatter(X, y, color='red', marker='+')
  plt.plot(Xtest, ypred, color='green')
  plt.plot(Xtest, ypred2, color='blue')
  plt.plot(Xtest, ypred3, color='orange')
plt.xlabel("input x"); plt.ylabel("output y")
plt.legend(["C=0.1","C=1","C=1000"])
plt.show()

df1=pd.read_csv("week6.csv", names=["Target","Value"]) 
#X=np.array(df1.iloc[:,0:1])
X=np.array(df1.iloc[:,0])
y=np.array(df1.iloc[:,-1])
X=X.reshape(-1, 1)
y=y.reshape(-1, 1)
Xtrain,Xtest,ytrain,ytest = train_test_split(X,y,test_size=0.25,random_state=0)
print(df1)

import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (12.0, 9.0)
# X = normalized_df
# Y = df.iloc[:, 1]
plt.scatter(X, y)
plt.xlabel('Target')
plt.ylabel('Value')
plt.show()

def gaussian_kernel100(distances):
  weights = np.exp(-(100 * (distances ** 2)))
  return weights/np.sum(weights)
def gaussian_kernel1000(distances):
  weights = np.exp(-(1000 * (distances ** 2)))
  return weights/np.sum(weights)
def gaussian_kernel10000(distances):
  weights = np.exp(-(10000 * (distances ** 2)))
  return weights/np.sum(weights)

model2 = KNeighborsRegressor(n_neighbors=1,weights=gaussian_kernel100).fit(Xtrain, ytrain)
ypred2 = model2.predict(Xtest)
model3 = KNeighborsRegressor(n_neighbors=10,weights=gaussian_kernel1000).fit(Xtrain, ytrain)
ypred3 = model3.predict(Xtest)
model4 = KNeighborsRegressor(n_neighbors=100,weights=gaussian_kernel10000).fit(Xtrain, ytrain)
ypred4 = model4.predict(Xtest)
plt.scatter(Xtrain, ytrain, color='red', marker='+')
plt.plot(Xtest, ypred2, color='blue')
plt.plot(Xtest, ypred3, color='orange')
plt.plot(Xtest, ypred4,color='green')
plt.xlabel("input x"); plt.ylabel("output y")
plt.legend(["k=1,sigma=100","k=10,sigma=1000","k=100,sigma=10000","train"])
plt.show()

import numpy as np
from sklearn.kernel_ridge import KernelRidge
gama_range = [0, 1, 5, 10, 25]
for gama in gama_range:
  model = KernelRidge(alpha=1.0/0.1, kernel='rbf', gamma=gama).fit(Xtrain, ytrain)
  ypred = model.predict(Xtest)
  model = KernelRidge(alpha=1.0/1, kernel='rbf', gamma=gama).fit(Xtrain, ytrain)
  ypred2 = model.predict(Xtest)
  model = KernelRidge(alpha=1.0/1000, kernel='rbf', gamma=gama).fit(Xtrain, ytrain)
  ypred3 = model.predict(Xtest)
  import matplotlib.pyplot as plt
  plt.rc('font', size=18); plt.rcParams['figure.constrained_layout.use'] = True
  plt.scatter(X, y, color='red', marker='+')
  plt.plot(Xtest, ypred, color='green')
  plt.plot(Xtest, ypred2, color='blue')
  plt.plot(Xtest, ypred3, color='orange')
plt.xlabel("input x"); plt.ylabel("output y")
plt.legend(["C=0.1","C=1","C=1000"])
plt.show()

mean_error=[]; std_error=[]
Ci_range = [1, 5, 10, 50, 100]
for Ci in Ci_range:
  model = KNeighborsClassifier(n_neighbors=Ci)
  temp=[]
  from sklearn.model_selection import KFold
  kf = KFold(n_splits=5)
  for train, test in kf.split(X):
    model.fit(X[train].astype('int'), y[train].astype('int'))
    ypred = model.predict(X[test])
    from sklearn.metrics import mean_squared_error
    temp.append(mean_squared_error(y[test],ypred))
  mean_error.append(np.array(temp).mean())
  std_error.append(np.array(temp).std())
import matplotlib.pyplot as plt
plt.errorbar(Ci_range,mean_error,yerr=std_error)
plt.xlabel('Ci'); plt.ylabel('Mean square error')
plt.xlim((0,100))
plt.show()

mean_error=[]; std_error=[]
folds = [2, 5, 10, 25, 50, 100]
c=1
for fold in folds:
    temp=[]
    kf = KFold(n_splits=fold)
    for train, test in kf.split(X): 
        model=Ridge(alpha=1/(2*fold)).fit(X[train],y[train])
        ypred = model.predict(X[test])
        mean=mean_squared_error(y[test],ypred)
        temp.append(mean)
    mean_error.append(np.array(temp).mean())
    std_error.append(np.array(temp).std()) 
plt.errorbar(folds,mean_error,yerr=std_error) 
plt.xlabel('folds'); 
plt.ylabel('Mean square error') 
plt.xlim((0,110))
plt.show()