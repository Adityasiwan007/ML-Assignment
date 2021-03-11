# -*- coding: utf-8 -*-
"""ML_Week4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pbImiZb3M-wzJ0BG-JzgBg42mPWPC6ef
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
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import roc_curve
from sklearn.model_selection import cross_val_score
from sklearn.metrics import auc

df1=pd.read_csv("week4_1.csv", names=["X1","X2","Target"]) 
X=np.array(df1.iloc[:,0:2])
y=df1.iloc[:,-1]
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=0)
print(df1)

pos = df1['Target'] == 1
neg = df1['Target'] == -1

fig, axes = pp.subplots();
axes.set_xlabel('X1')
axes.set_ylabel('X2')
axes.scatter(df1.loc[pos, 'X1'], df1.loc[pos, 'X2'], color = 'g', marker='+', label='+1')
axes.scatter(df1.loc[neg, 'X1'], df1.loc[neg, 'X2'], color = 'r', marker='o', label='-1')
axes.legend(title='Sign', loc = 'best' )
axes.set_xlim(-1,1)

num_features = list()
degress = [i for i in range(1, 6)]
for d in degress:
	trans = PolynomialFeatures(degree=d)
	data = trans.fit_transform(X)
	num_features.append(data.shape[1])
	print('Degree: %d, Features: %d' % (d, data.shape[1]))
pyplot.plot(degress, num_features)
pyplot.xlabel('Degree')
pyplot.ylabel('Features')
pyplot.show()

mean_error=[]; std_error=[]
Ci_range = [0.1, 0.5, 1, 5, 10, 50, 100]
for Ci in Ci_range:
  model = LogisticRegression(C=Ci)
  temp=[]
  from sklearn.model_selection import KFold
  kf = KFold(n_splits=5)
  for train, test in kf.split(X):
    model.fit(X[train], y[train])
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
Ci_range = [1, 5, 10, 50, 100]
for Ci in Ci_range:
  model = KNeighborsClassifier(n_neighbors=Ci)
  temp=[]
  from sklearn.model_selection import KFold
  kf = KFold(n_splits=5)
  for train, test in kf.split(X):
    model.fit(X[train], y[train])
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

kf = KFold(n_splits=5)
plt.rc('font', size=18); plt.rcParams['figure.constrained_layout.use'] = True
mean_error=[]; std_error=[]
q_range = [1,2,3,4,5,6]
for q in q_range:
  Xpoly = PolynomialFeatures(q).fit_transform(X)
  model = LogisticRegression()
  temp=[]; plotted = False
  for train, test in kf.split(Xpoly):
    model.fit(Xpoly[train], y[train])
    ypred = model.predict(Xpoly[test])
    from sklearn.metrics import mean_squared_error
    temp.append(mean_squared_error(y[test],ypred))
  mean_error.append(np.array(temp).mean())
  std_error.append(np.array(temp).std())
plt.errorbar(q_range,mean_error,yerr=std_error,linewidth=3)
plt.xlabel('q')
plt.ylabel('Mean square error')
plt.show()

kf = KFold(n_splits=5)
plt.rc('font', size=18); plt.rcParams['figure.constrained_layout.use'] = True
mean_error=[]; std_error=[]
q_range = [1,2,3,4,5,6]
for q in q_range:
  Xpoly = PolynomialFeatures(q).fit_transform(X)
  model = KNeighborsClassifier(n_neighbors=3)
  temp=[]; plotted = False
  for train, test in kf.split(Xpoly):
    model.fit(Xpoly[train], y[train])
    ypred = model.predict(Xpoly[test])
    from sklearn.metrics import mean_squared_error
    temp.append(mean_squared_error(y[test],ypred))
  mean_error.append(np.array(temp).mean())
  std_error.append(np.array(temp).std())
plt.errorbar(q_range,mean_error,yerr=std_error,linewidth=3)
plt.xlabel('q')
plt.ylabel('Mean square error')
plt.show()

logistic_regression= LogisticRegression()
logistic_regression.fit(X_train,y_train)
y_pred=logistic_regression.predict(X_test)
confusion_matrix = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted'])
sn.heatmap(confusion_matrix, annot=True)
print(confusion_matrix)
print('Accuracy: ',metrics.accuracy_score(y_test, y_pred))
plt.show()

kNeighborsClassifier= KNeighborsClassifier(n_neighbors=3)
kNeighborsClassifier.fit(X_train,y_train)
y_pred=kNeighborsClassifier.predict(X_test)
confusion_matrix = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted'])
sn.heatmap(confusion_matrix, annot=True)
print(confusion_matrix)
print('Accuracy: ',metrics.accuracy_score(y_test, y_pred))
plt.show()

plt.rc('font', size=18); plt.rcParams['figure.constrained_layout.use'] = True
logistic_regression= LogisticRegression()
model = logistic_regression.fit(X_train, y_train)
fpr, tpr, _ = roc_curve(y_test,model.decision_function(X_test))
roc_auc = auc(fpr, tpr)
plt.plot(fpr, tpr, 'b', label = 'AUC = %0.4f' % roc_auc)
plt.legend(loc = 'lower right')
plt.plot([-1, 1], [-1, 1],'r--')
plt.xlim([-.1, 1])
plt.ylim([0, 1.1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.title('ROC Curve of LogisticRegression')
plt.show()

plt.rc('font', size=18); plt.rcParams['figure.constrained_layout.use'] = True
kNeighborsClassifier= KNeighborsClassifier(n_neighbors=3)
knn = kNeighborsClassifier.fit(X_train, y_train)
y_scores = knn.predict_proba(X_test)
fpr, tpr, threshold = roc_curve(y_test, y_scores[:, 1])
roc_auc = auc(fpr, tpr)
plt.plot(fpr, tpr, 'b', label = 'AUC = %0.4f' % roc_auc)
plt.legend(loc = 'lower right')
plt.plot([-1, 1], [-1, 1],'r--')
plt.xlim([-.1, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.title('ROC Curve of kNN')
plt.show()

# for noisy data week4_2
df2=pd.read_csv("week4_2.csv", names=["X1","X2","Value"]) 
X=np.array(df2.iloc[:,0:2])
y=df2.iloc[:,-1]
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=0)
print(df2)

pos = df2['Value'] == 1
neg = df2['Value'] == -1

fig, axes = pp.subplots();
axes.set_xlabel('X1')
axes.set_ylabel('X2')
axes.scatter(df2.loc[pos, 'X1'], df2.loc[pos, 'X2'], color = 'g', marker='+', label='+1')
axes.scatter(df2.loc[neg, 'X1'], df2.loc[neg, 'X2'], color = 'r', marker='o', label='-1')
axes.legend(title='Sign', loc = 'best' )
axes.set_xlim(-1,1)

num_features = list()
degress = [i for i in range(1, 6)]
for d in degress:
	trans = PolynomialFeatures(degree=d)
	data = trans.fit_transform(X)
	num_features.append(data.shape[1])
	print('Degree: %d, Features: %d' % (d, data.shape[1]))
pyplot.plot(degress, num_features)
pyplot.xlabel('Degree')
pyplot.ylabel('Features')
pyplot.show()

mean_error=[]; std_error=[]
Ci_range = [0.1, 0.5, 1, 5, 10, 50, 100]
for Ci in Ci_range:
  model = LogisticRegression(C=Ci)
  temp=[]
  from sklearn.model_selection import KFold
  kf = KFold(n_splits=5)
  for train, test in kf.split(X):
    model.fit(X[train], y[train])
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
Ci_range = [1, 5, 10, 50, 100]
for Ci in Ci_range:
  model = KNeighborsClassifier(n_neighbors=Ci)
  temp=[]
  from sklearn.model_selection import KFold
  kf = KFold(n_splits=5)
  for train, test in kf.split(X):
    model.fit(X[train], y[train])
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

kf = KFold(n_splits=5)
plt.rc('font', size=18); plt.rcParams['figure.constrained_layout.use'] = True
mean_error=[]; std_error=[]
q_range = [1,2,3,4,5,6]
for q in q_range:
  Xpoly = PolynomialFeatures(q).fit_transform(X)
  model = LogisticRegression()
  temp=[]; plotted = False
  for train, test in kf.split(Xpoly):
    model.fit(Xpoly[train], y[train])
    ypred = model.predict(Xpoly[test])
    from sklearn.metrics import mean_squared_error
    temp.append(mean_squared_error(y[test],ypred))
  mean_error.append(np.array(temp).mean())
  std_error.append(np.array(temp).std())
plt.errorbar(q_range,mean_error,yerr=std_error,linewidth=3)
plt.xlabel('q')
plt.ylabel('Mean square error')
plt.show()

kf = KFold(n_splits=5)
plt.rc('font', size=18); plt.rcParams['figure.constrained_layout.use'] = True
mean_error=[]; std_error=[]
q_range = [1,2,3,4,5,6]
for q in q_range:
  Xpoly = PolynomialFeatures(q).fit_transform(X)
  model = KNeighborsClassifier(n_neighbors=3)
  temp=[]; plotted = False
  for train, test in kf.split(Xpoly):
    model.fit(Xpoly[train], y[train])
    ypred = model.predict(Xpoly[test])
    from sklearn.metrics import mean_squared_error
    temp.append(mean_squared_error(y[test],ypred))
  mean_error.append(np.array(temp).mean())
  std_error.append(np.array(temp).std())
plt.errorbar(q_range,mean_error,yerr=std_error,linewidth=3)
plt.xlabel('q')
plt.ylabel('Mean square error')
plt.show()

logistic_regression= LogisticRegression()
logistic_regression.fit(X_train,y_train)
y_pred=logistic_regression.predict(X_test)
confusion_matrix = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted'])
sn.heatmap(confusion_matrix, annot=True)
print(confusion_matrix)
print('Accuracy: ',metrics.accuracy_score(y_test, y_pred))
plt.show()

kNeighborsClassifier= KNeighborsClassifier(n_neighbors=3)
kNeighborsClassifier.fit(X_train,y_train)
y_pred=kNeighborsClassifier.predict(X_test)
confusion_matrix = pd.crosstab(y_test, y_pred, rownames=['Actual'], colnames=['Predicted'])
sn.heatmap(confusion_matrix, annot=True)
print(confusion_matrix)
print('Accuracy: ',metrics.accuracy_score(y_test, y_pred))
plt.show()

plt.rc('font', size=18); plt.rcParams['figure.constrained_layout.use'] = True
logistic_regression= LogisticRegression()
model = logistic_regression.fit(X_train, y_train)
fpr, tpr, _ = roc_curve(y_test,model.decision_function(X_test))
roc_auc = auc(fpr, tpr)
plt.plot(fpr, tpr, 'b', label = 'AUC = %0.4f' % roc_auc)
plt.legend(loc = 'lower right')
plt.plot([-1, 1], [-1, 1],'r--')
plt.xlim([-.1, 1])
plt.ylim([0, 1.1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.title('ROC Curve of LogisticRegression')
plt.show()

plt.rc('font', size=18); plt.rcParams['figure.constrained_layout.use'] = True
kNeighborsClassifier= KNeighborsClassifier(n_neighbors=3)
knn = kNeighborsClassifier.fit(X_train, y_train)
y_scores = knn.predict_proba(X_test)
fpr, tpr, threshold = roc_curve(y_test, y_scores[:, 1])
roc_auc = auc(fpr, tpr)
plt.plot(fpr, tpr, 'b', label = 'AUC = %0.4f' % roc_auc)
plt.legend(loc = 'lower right')
plt.plot([-1, 1], [-1, 1],'r--')
plt.xlim([-.1, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.title('ROC Curve of kNN')
plt.show()