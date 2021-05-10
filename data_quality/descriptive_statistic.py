import pandas as pd
import numpy as np
import io
# import pandas_profiling

retail_raw = pd.read_csv('./datasets/retail_raw_reduced_data_quality.csv')

# print(retail_raw.dtypes)

# Column city length
length_city = len(retail_raw['city'])
print(length_city)

# Column city count
count_city = retail_raw['city'].count()
# print(count_city)

number_of_missing_values_city = length_city - count_city
float_of_missing_values_city = float(number_of_missing_values_city/length_city)
pct_of_missing_values_city = '{0:.1f}%'.format(float_of_missing_values_city * 100)
# print(pct_of_missing_values_city)

# Descriptive statistics column quantity
print('Kolom quantity')
print('Minimum value: ', retail_raw['quantity'].min())
print('Maximum value: ', retail_raw['quantity'].max())
print('Mean value: ', retail_raw['quantity'].mean())
print('Mode value: ', retail_raw['quantity'].mode())
print('Median value: ', retail_raw['quantity'].median())
print('Standard Deviation value: ', retail_raw['quantity'].std())

# Quantile statistics column quantity
print('Kolom quantity:')
print(retail_raw['quantity'].quantile([0.25, 0.5, 0.75]))

# Correlation between quantity and item_price
print(retail_raw[['quantity', 'item_price']].corr())