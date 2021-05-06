import pandas as pd
import matplotlib.pyplot as plt

order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")

# plot histogram column: price
order_df[["price"]].hist(figsize=(3, 7), bins=10, xlabelsize=8, ylabelsize=8)
plt.show()