import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import confusion_matrix, classification_report
import pickle
from pathlib import Path

df_load = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/dqlab_telco_final.csv')
# print(df_load.shape)
# print(df_load.head())
# print(df_load.customerID.nunique())

# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])
# ax.axis('equal')
# labels = ['Yes','No']
# churn = df_load.Churn.value_counts()
# ax.pie(churn, labels=labels, autopct='%.0f%%')
# plt.show()

# #creating bin in chart
# numerical_features = ['MonthlyCharges','TotalCharges','tenure']
# fig, ax = plt.subplots(1, 3, figsize=(15, 6))
# # Use the following code to plot two overlays of histogram per each numerical_features, use a color of blue and orange, respectively
# df_load[df_load.Churn == 'No'][numerical_features].hist(bins=20, color='blue', alpha=0.5, ax=ax)
# df_load[df_load.Churn == 'Yes'][numerical_features].hist(bins=20, color='orange', alpha=0.5, ax=ax)
# plt.show()

# sns.set(style='darkgrid')
# # Your code goes here
# fig, ax = plt.subplots(3, 3, figsize=(14, 12))
# sns.countplot(data=df_load, x='gender', hue='Churn', ax=ax[0][0])
# sns.countplot(data=df_load, x='Partner', hue='Churn', ax=ax[0][1])
# sns.countplot(data=df_load, x='SeniorCitizen', hue='Churn', ax=ax[0][2])
# sns.countplot(data=df_load, x='PhoneService', hue='Churn', ax=ax[1][0])
# sns.countplot(data=df_load, x='StreamingTV', hue='Churn', ax=ax[1][1])
# sns.countplot(data=df_load, x='InternetService', hue='Churn', ax=ax[1][2])
# sns.countplot(data=df_load, x='PaperlessBilling', hue='Churn', ax=ax[2][1])
# plt.tight_layout()
# plt.show()

#Remove the unnecessary columns customerID & UpdatedAt
cleaned_df = df_load.drop(['customerID','UpdatedAt'], axis=1)
# print(cleaned_df.head())

#Convert all the non-numeric columns to numerical data types
for column in cleaned_df.columns:
    if cleaned_df[column].dtype == np.float64:
        continue
    # Perform encoding for each non-numeric column
    cleaned_df[column] = LabelEncoder().fit_transform(cleaned_df[column])
# print(cleaned_df.describe())

# Predictor dan target
X = cleaned_df.drop('Churn', axis = 1)
y = cleaned_df['Churn']
# Splitting train and test
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
# Print according to the expected result
# print('Jumlah baris dan kolom dari x_train adalah:', x_train.shape,', sedangkan Jumlah baris dan kolom dari y_train adalah:', y_train.shape)
# print('Prosentase Churn di data Training adalah:')
# print(y_train.value_counts(normalize=True))
# print('Jumlah baris dan kolom dari x_test adalah:', x_test.shape,', sedangkan Jumlah baris dan kolom dari y_test adalah:', y_test.shape)
# print('Prosentase Churn di data Testing adalah:')
# print(y_test.value_counts(normalize=True))

log_model = LogisticRegression(solver='lbfgs', max_iter=10000).fit(x_train, y_train)
# print('Model Logistic Regression yang terbentuk adalah: \n',log_model)

# Predict
y_train_pred = log_model.predict(x_train)
# Print classification report
# print('Classification Report Training Model (Logistic Regression) :')
# print(classification_report(y_train, y_train_pred))

# # Form confusion matrix as a DataFrame
# confusion_matrix_df = pd.DataFrame((confusion_matrix(y_train, y_train_pred)), ('No churn', 'Churn'), ('No churn', 'Churn'))

# # Plot confusion matrix
# plt.figure()
# heatmap = sns.heatmap(confusion_matrix_df, annot=True, annot_kws={'size': 14}, fmt='d', cmap='YlGnBu')
# heatmap.yaxis.set_ticklabels(heatmap.yaxis.get_ticklabels(), rotation=0, ha='right', fontsize=14)
# heatmap.xaxis.set_ticklabels(heatmap.xaxis.get_ticklabels(), rotation=0, ha='right', fontsize=14)

# plt.title('Confusion Matrix for Training Model\n(Logistic Regression)', fontsize=18, color='darkblue')
# plt.ylabel('True label', fontsize=14)
# plt.xlabel('Predicted label', fontsize=14)
# plt.show()

# Predict
y_test_pred = log_model.predict(x_test)
# Print classification report
# print('Classification Report Testing Model (Logistic Regression):')
# print(classification_report(y_test, y_test_pred))

# Form confusion matrix as a DataFrame
confusion_matrix_df = pd.DataFrame((confusion_matrix(y_test, y_test_pred)), ('No churn', 'Churn'), ('No churn', 'Churn'))

# Plot confusion matrix
plt.figure()
heatmap = sns.heatmap(confusion_matrix_df, annot=True, annot_kws={'size': 14}, fmt='d', cmap='YlGnBu')
heatmap.yaxis.set_ticklabels(heatmap.yaxis.get_ticklabels(), rotation=0, ha='right', fontsize=14)
heatmap.xaxis.set_ticklabels(heatmap.xaxis.get_ticklabels(), rotation=0, ha='right', fontsize=14)

plt.title('Confusion Matrix for Testing Model\n(Logistic Regression)\n', fontsize=18, color='darkblue')
plt.ylabel('True label', fontsize=14)
plt.xlabel('Predicted label', fontsize=14)
plt.show()