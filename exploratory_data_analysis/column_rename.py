import pandas as pd

order_df = pd.read_csv("./datasets/order.csv")

# Rename freight_value into shipping_cost
order_df.rename(columns={"freight_value": "shipping_cost"}, inplace=True)
print(order_df)