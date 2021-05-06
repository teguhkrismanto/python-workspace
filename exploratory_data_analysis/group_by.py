import pandas as pd

order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")

# Calculate the average price per payment_type
mean = order_df["price"].groupby(order_df["payment_type"]).mean()
print(mean)