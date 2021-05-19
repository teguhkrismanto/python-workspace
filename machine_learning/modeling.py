import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, classification_report

dataset = pd.read_csv('./datasets/online_raw.csv')

# removing the target column Revenue from dataset and assigning to X
X = dataset.drop(['Revenue'], axis = 1)
# assigning the target column Revenue to y
y = dataset['Revenue']
# # checking the shapes
# print("Shape of X:", X.shape)
# print("Shape of y:", y.shape)

# splitting the X, and y
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
# checking the shapes
# print("Shape of X_train :", X_train.shape)
# print("Shape of y_train :", y_train.shape)
# print("Shape of X_test :", X_test.shape)
# print("Shape of y_test :", y_test.shape)

# Call the classifier
model = DecisionTreeClassifier()
# Fit the classifier to the training data
model = model.fit(X_train, y_train, sample_weight=None)

# Apply the classifier/model to the test data
y_pred = model.predict(X_test)
print(y_pred.shape)

# evaluating the model
print('Training Accuracy :', model.score(X_train, y_train))
print('Testing Accuracy :', model.score(X_test, y_test))

# confusion matrix
print('\nConfusion matrix:')
cm = confusion_matrix(y_test, y_pred)
print(cm)