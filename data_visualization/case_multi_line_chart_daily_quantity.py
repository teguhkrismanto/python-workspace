import datetime
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('./datasets/retail_raw_reduced.csv')
dataset['order_month'] = dataset['order_date'].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m'))

# Take information on top 5 brands by quantity
top_brands = (dataset[dataset['order_month']=='2019-12'].groupby('brand')['quantity']
                                                        .sum()
                                                        .reset_index()
                                                        .sort_values(by='quantity',ascending=False)
                                                        .head(5))

# Created a new dataframe, filtered only in December 2019 and only top 5 brands
dataset_top5brand_dec = dataset[(dataset['order_month']=='2019-12') & (dataset['brand'].isin(top_brands['brand'].to_list()))]
dataset_top5brand_dec.groupby(['order_date','brand'])['quantity'].sum().unstack().plot(marker='.', cmap='plasma')

plt.title('Daily Sold Quantity Dec 2019 - Breakdown by Brands',loc='center',pad=30, fontsize=15, color='blue')
plt.xlabel('Order Date', fontsize = 12)
plt.ylabel('Quantity',fontsize = 12)
plt.grid(color='darkgray', linestyle=':', linewidth=0.5)
plt.ylim(ymin=0)
plt.legend(loc='upper center', bbox_to_anchor=(1.1, 1), shadow=True, ncol=1)
plt.annotate('Terjadi lonjakan', xy=(7, 310), xytext=(8, 300),
            weight='bold', color='red',
            arrowprops=dict(arrowstyle='->',
            connectionstyle="arc3",
            color='red'))
plt.gcf().set_size_inches(10, 5)
plt.tight_layout()
plt.show()