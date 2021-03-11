# -*- coding: utf-8 -*-
"""ML_Week2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kUCUZxSx4OA5mXJHEAyqzNsZcFBFQOGZ
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as pp
# %matplotlib inline

df=pd.read_csv("week2.csv", names=["X1","X2","Value"]) 

X1=np.array(df.iloc[:,0])
X1=X1.reshape(-1, 1)
X2=np.array(df.iloc[:,1])
X2=X2.reshape(-1, 1)
Value=df.iloc[:,-1]
X=np.column_stack((X1,X2)) 
print(df)

pos = df['Value'] == 1
neg = df['Value'] == -1

fig, axes = pp.subplots();
axes.set_xlabel('X1')
axes.set_ylabel('X2')
axes.scatter(df.loc[pos, 'X1'], df.loc[pos, 'X2'], color = 'g', marker='+', label='+1')
axes.scatter(df.loc[neg, 'X1'], df.loc[neg, 'X2'], color = 'r', marker='o', label='-1')
axes.legend(title='Sign', loc = 'best' )
axes.set_xlim(-1,1)
axes.set_xlim(-1,1)

def mapFeature(X1, X2, degree):
    r = np.ones(X1.shape[0])
    for i in range(1,degree + 1):
        for j in range(0,i + 1):
            r = np.column_stack((r, (X1 ** (i-j)) * (X2 ** j)))
    
    return r

X = df.iloc[:, :2]
degree = 2
X_poly = mapFeature(X.iloc[:, 0], X.iloc[:, 1], degree)
y = df.iloc[:, 2]

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def costFunc(theta, X, y):
    m = y.shape[0]
    z = X.dot(theta)
    h = sigmoid(z)
    term1 = y * np.log(h)
    term2 = (1- y) * np.log(1 - h)
    J = -np.sum(term1 + term2, axis = 0) / m
    return J

initial_theta = np.zeros(X_poly.shape[1]).reshape(X_poly.shape[1], 1)
from scipy.optimize import minimize
res = minimize(costFunc, initial_theta, args=(X_poly, y))
theta = res.x

def plotDecisionBoundary(theta,degree, axes):
    u = np.linspace(-1, 1, 50)
    v = np.linspace(-1, 1, 50)
    U,V = np.meshgrid(u,v)
    U = np.ravel(U)
    V = np.ravel(V)
    Z = np.zeros((len(u) * len(v)))
    
    X_poly = mapFeature(U, V, degree)
    Z = X_poly.dot(theta)
    U = U.reshape((len(u), len(v)))
    V = V.reshape((len(u), len(v)))
    Z = Z.reshape((len(u), len(v)))
    
    cs = axes.contour(U,V,Z,levels=[0],cmap= "Dark2")
    axes.legend(labels=['+1', '-1', 'Decision Boundary'])
    return cs

fig, axes = pp.subplots();
axes.set_xlabel('X1')
axes.set_ylabel('X2')
axes.scatter(df.loc[pos, 'X1'], df.loc[pos, 'X2'], color = 'r', marker='x', label='+1')
axes.scatter(df.loc[neg, 'X1'], df.loc[neg, 'X2'], color = 'g', marker='o', label='-1')

plotDecisionBoundary(theta, degree, axes)

def costFuncReg(theta, X, y, reg_factor):
    m = y.shape[0]
    z = X.dot(theta)
    h = sigmoid(z)
    term1 = y * np.log(h)
    term2 = (1- y) * np.log(1 - h)
    J = -np.sum(term1 + term2, axis = 0) / m
    
    # Regularization Term
    reg_term = (reg_factor * sum(theta[1:] ** 2)) / (2 * m)
    J = J + reg_term
    return J

# Set the regularization factor to 1
reg_factor = 100
degree = 6
# map features to the degree
X_poly = mapFeature(X.iloc[:, 0], X.iloc[:, 1], degree)
# set initial parameters
initial_theta = np.zeros(X_poly.shape[1]).reshape(X_poly.shape[1], 1)

res = minimize(costFuncReg, initial_theta, args=(X_poly, y, reg_factor))
theta = res.x.reshape(res.x.shape[0], 1)

# Plot Decision boundary
fig, axes = pp.subplots();
axes.set_xlabel('Feature 1')
axes.set_ylabel('Feature 2')
axes.scatter(df.loc[pos, 'X1'], df.loc[pos, 'X2'], color = 'r', marker='x', label='+1')
axes.scatter(df.loc[neg, 'X1'], df.loc[neg, 'X2'], color = 'g', marker='o', label='-1')
#axes.legend(title='Legend', loc = 'best' )

plotDecisionBoundary(theta, degree, axes)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics, svm
import seaborn as sn
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn import utils
X_df = df[['X1','X2']]
y_df = df['Value']
X_train,X_test,y_train,y_test = train_test_split(X_df,y_df,test_size=0.25,random_state=0)

lab_enc = preprocessing.LabelEncoder()
training_scores_encoded = lab_enc.fit_transform(y_train)

logistic_regression= LogisticRegression()
logistic_regression.fit(X_train,y_train)
y_pred=logistic_regression.predict(X_test)

print (y_test) #test dataset
print (y_pred) #predicted values

confusion_matrix = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted'])
sn.heatmap(confusion_matrix, annot=True)
print(confusion_matrix)
print('Accuracy: ',metrics.accuracy_score(y_test.round(), y_pred))
plt.show()

from sklearn.datasets import make_blobs
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
X=X_df
y=y_df
model = LogisticRegression()
# fit the model
model.fit(X, y)
# make predictions
yhat = model.predict(X)
# evaluate the predictions
acc = accuracy_score(y, yhat)
print('Accuracy: %.3f' % acc)

from numpy import where
from numpy import meshgrid
from numpy import arange
from numpy import hstack
from sklearn.datasets import make_blobs
from sklearn.linear_model import LogisticRegression
from matplotlib import pyplot
pos = df['Value'] == 1
neg = df['Value'] == -1

min1, max1 = -1,1.1
min2, max2 = -1,1.1

x1grid = arange(min1, max1, 0.1)
x2grid = arange(min2, max2, 0.1)

xx, yy = meshgrid(x1grid, x2grid)

r1, r2 = xx.flatten(), yy.flatten()
r1, r2 = r1.reshape((len(r1), 1)), r2.reshape((len(r2), 1))

grid = hstack((r1,r2))
model = LogisticRegression()
model.fit(X, y)
yhat = model.predict(grid)
zz = yhat.reshape(xx.shape)
pyplot.contourf(xx, yy, zz, cmap='Paired')
for class_value in [1,-1]:
	row_ix = where(y == class_value)
pyplot.scatter(df.loc[pos, 'X1'], df.loc[pos, 'X2'], color = 'g', marker='+', label='+1')
pyplot.scatter(df.loc[neg, 'X1'], df.loc[neg, 'X2'], color = 'r', marker='o', label='-1')
pyplot.legend(title='Sign', loc = 'best' )

clf = svm.SVC(kernel='linear',C = 100) # Linear Kernel

#Train the model using the training sets
clf.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)

# Model Accuracy: how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

print("Precision:",metrics.precision_score(y_test, y_pred))

# Model Recall: what percentage of positive tuples are labelled as such?
print("Recall:",metrics.recall_score(y_test, y_pred))

plt.scatter(df.loc[pos, 'X1'], df.loc[pos, 'X2'], color = 'g', marker='+', label='+1')
plt.scatter(df.loc[neg, 'X1'], df.loc[neg, 'X2'], color = 'r', marker='o', label='-1')
ax = plt.gca()
xlim = ax.get_xlim()
w = clf.coef_[0]
a = -w[0] / w[1]
xx = np.linspace(xlim[0], xlim[1])
yy = a * xx - clf.intercept_[0] / w[1]
plt.plot(xx, yy)
yy = a * xx - (clf.intercept_[0] - 1) / w[1]
plt.plot(xx, yy, 'k--')
yy = a * xx - (clf.intercept_[0] + 1) / w[1]
plt.plot(xx, yy, 'k--')

from sklearn.preprocessing import PolynomialFeatures
num_features = list()
degress = [i for i in range(1, 6)]
for d in degress:
	# create transform
	trans = PolynomialFeatures(degree=d)
	# fit and transform
	data = trans.fit_transform(X)
	# record number of features
	num_features.append(data.shape[1])
	# summarize
	print('Degree: %d, Features: %d' % (d, data.shape[1]))
# plot degree vs number of features
pyplot.plot(degress, num_features)
pyplot.show()

from numpy import mean
from numpy import std
from pandas import read_csv
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from matplotlib import pyplot

 
# get a list of models to evaluate
def get_models():
	models = dict()
	for d in range(1,5):
		# define the pipeline
		trans = PolynomialFeatures(degree=d)
		model = KNeighborsClassifier()
		models[str(d)] = Pipeline(steps=[('t', trans), ('m', model)])
	return models
 
# evaluate a give model using cross-validation
def evaluate_model(model, X, y):
	cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
	scores = cross_val_score(model, X, y, scoring='accuracy', cv=cv, n_jobs=-1, error_score='raise')
	return scores
 
# get the models to evaluate
models = get_models()
# evaluate the models and store results
results, names = list(), list()
for name, model in models.items():
	scores = evaluate_model(model, X, y)
	results.append(scores)
	names.append(name)
	print('>%s %.3f (%.3f)' % (name, mean(scores), std(scores)))
# plot model performance for comparison
pyplot.boxplot(results, labels=names, showmeans=True)
pyplot.show()