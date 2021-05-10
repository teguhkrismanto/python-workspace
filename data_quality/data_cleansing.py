import pandas as pd
import numpy as np
import io
# import pandas_profiling

retail_raw = pd.read_csv('./datasets/retail_raw_reduced_data_quality.csv')

print('Check the column that has missing data:')
print(retail_raw.isnull().any())

# Filling the missing value (imputation)
print('\nFilling the missing value (imputation):')
print(retail_raw['quantity'].fillna(retail_raw.quantity.mean()))

# Drop missing value
print('\nDrop missing value:')

print(retail_raw['item_price'].fillna(retail_raw['item_price'].mean()))

# Q1, Q3, dan IQR
Q1 = retail_raw['quantity'].quantile(0.25)
Q3 = retail_raw['quantity'].quantile(0.75)
IQR = Q3 - Q1

# Check sizes (rows and columns) before data outliers are discarded
print('Shape awal: ', retail_raw.shape)

# Removing outliers
retail_raw = retail_raw[~((retail_raw['quantity'] < (Q1 - 1.5 * IQR)) | (retail_raw['quantity'] > (Q3 + 1.5 * IQR)))]

# Check the size (rows and columns) after the data outliers are discarded
print('Shape akhir: ', retail_raw.shape)

# Discard duplicated data
retail_raw.drop_duplicates(inplace=True)