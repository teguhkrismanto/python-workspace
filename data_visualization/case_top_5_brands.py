import datetime
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/retail_raw_reduced.csv')
dataset['order_month'] = dataset['order_date'].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))

# Take information on top 5 brands by quantity
top_brands = (dataset[dataset['order_month']=='2019-12'].groupby('brand')['quantity']
                                                        .sum()
                                                        .reset_index()
                                                        .sort_values(by='quantity',ascending=False)
                                                        .head(5))

# Created a new dataframe, filtered only in December 2019 and only top 5 brands
dataset_top5brand_dec = dataset[(dataset['order_month']=='2019-12') & (dataset['brand'].isin(top_brands['brand'].to_list()))]

print(top_brands)