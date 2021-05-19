import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/pythonTutorial/online_raw.csv')
# print('Shape dataset:', dataset.shape)
# print('\nLima data teratas:\n', dataset.head())
# print('\nInformasi dataset:')
# print(dataset.info())
# print('\nStatistik deskriptif:\n', dataset.describe())

# dataset_corr = dataset.corr()
# print('Korelasi dataset:\n', dataset.corr())
# print('Distribusi Label (Revenue):\n', dataset['Revenue'].value_counts())
# # Tugas praktek
# print('\nKorelasi BounceRates-ExitRates:', dataset_corr.loc['BounceRates', 'ExitRates'])
# print('\nKorelasi Revenue-PageValues:', dataset_corr.loc['Revenue', 'PageValues'])
# print('\nKorelasi TrafficType-Weekend:', dataset_corr.loc['TrafficType', 'Weekend'])

# # checking the Distribution of customers on Revenue
# plt.rcParams['figure.figsize'] = (12,5)
# plt.subplot(1, 2, 1)
# sns.countplot(dataset['Revenue'], palette = 'pastel')
# plt.title('Buy or not', fontsize = 20)
# plt.xlabel('Revenue or not', fontsize = 14)
# plt.ylabel('count', fontsize = 14)
# # checking the Distribution of customers on Weekend
# plt.subplot(1, 2, 2)
# sns.countplot(dataset['Weekend'], palette = 'inferno')
# plt.title('Purchase on Weekends', fontsize = 20)
# plt.xlabel('Weekend or not', fontsize = 14)
# plt.ylabel('count', fontsize = 14)
# plt.show()

# #checking missing value for each feature
# print('Checking missing value for each feature:')
# print(dataset.isnull().sum())
# #Counting total missing value
# print('\nCounting total missing value:')
# print(dataset.isnull().sum().sum())

# #Drop rows with missing value
# dataset_clean = dataset.dropna()
# print('Ukuran dataset_clean:', dataset_clean.shape)

# print("Before imputation:")
# # Checking missing value for each feature
# print(dataset.isnull().sum())
# # Counting total missing value
# print(dataset.isnull().sum().sum())

# print("\nAfter imputation:")
# # Fill missing value with mean of feature value
# dataset.fillna(dataset.mean(), inplace = True)
# # Checking missing value for each feature
# print(dataset.isnull().sum())
# # Counting total missing value
# print(dataset.isnull().sum().sum())

# #Define MinMaxScaler as scaler
# scaler = MinMaxScaler()
# #list all the feature that need to be scaled
# scaling_column = ['Administrative','Administrative_Duration','Informational','Informational_Duration','ProductRelated','ProductRelated_Duration','BounceRates','ExitRates','PageValues']
# #Apply fit_transfrom to scale selected feature
# dataset[scaling_column] = scaler.fit_transform(dataset[scaling_column])
# #Cheking min and max value of the scaling_column
# print(dataset[scaling_column].describe().T[['min','max']])

# Convert feature/column 'Month'
LE = LabelEncoder()
dataset['Month'] = LE.fit_transform(dataset['Month'])
print(LE.classes_)
print(np.sort(dataset['Month'].unique()))
print('')

# Convert feature/column 'VisitorType'
LE = LabelEncoder()
dataset['VisitorType'] = LE.fit_transform(dataset['VisitorType'])
print(LE.classes_)
print(np.sort(dataset['VisitorType'].unique()))