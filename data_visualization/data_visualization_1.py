import pandas as pd
import datetime
import matplotlib.pyplot as plt

dataset = pd.read_csv('./datasets/retail_raw_reduced.csv')
dataset['order_month'] = dataset['order_date'].apply(lambda x: datetime.datetime.strptime(x, "%Y-%m-%d").strftime('%Y-%m')) # Addition of Order Month Column to Dataset
dataset['gmv'] = dataset['item_price']*dataset['quantity'] # Addition of GMV Columns to the Dataset

monthly_amount = dataset.groupby('order_month')['gmv'].sum().reset_index() # Create Aggregate Data

fig = plt.figure(figsize=(10,5)) # Change the Figure Size

# plt.plot(monthly_amount['order_month'], monthly_amount['gmv']) # First Plot: Creating a GMV Growth Trend Line Charts
dataset.groupby(['order_month'])['gmv'].sum().plot(color='green', marker='o', linestyle='-.', linewidth=2) # Alternative way: Function .plot () on pandas Dataframe and Line and Point Customization

# Added Title and Axis Labels and Customize Title and Axis Labels
plt.title('Monthly GMV Year 2019', loc='center', pad=40, fontsize=20, color='blue')
plt.xlabel('Order Month', fontsize=15)
plt.ylabel('Total Amount', fontsize=15)

plt.grid(color='darkgray', linestyle=':', linewidth=0.5) # Grid Customization
plt.ylim(ymin=0) # Set Minimum and Maximum Axis Ticks

# Customize Axis Ticks
labels, locations = plt.yticks()
plt.yticks(labels, (labels/1000000000).astype(int))

plt.text(0.45, 0.72, 'The GMV increased significantly on October 2019', transform=fig.transFigure, color='red') # Adding Information to the Plot

# print(dataset.head())
# plt.savefig('monthly_gmv.png', quality=95)
plt.show()

