import pandas as pd

order_df = pd.read_csv("./datasets/order.csv")

# Sort by price
price_sort = order_df.sort_values(by="price", ascending=0)
print(price_sort)