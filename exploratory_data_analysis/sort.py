import pandas as pd

order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")

# Sort by price
price_sort = order_df.sort_values(by="price", ascending=0)
print(price_sort)