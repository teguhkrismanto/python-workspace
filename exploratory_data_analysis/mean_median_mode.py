import pandas as pd

order_df = pd.read_csv("./datasets/order.csv")

# print(order_df.describe())

# Display Mean
print(order_df.loc[:, "quantity"].mean())
print(order_df.loc[:, "price"].mean())
print(order_df.loc[:, "freight_value"].mean())
print(order_df.loc[:, "product_weight_gram"].mean())

# Display median
# print(order_df.loc[:, "quantity"].median())
# print(order_df.loc[:, "price"].median())
# print(order_df.loc[:, "freight_value"].median())
# print(order_df.loc[:, "product_weight_gram"].median())

# Display mode
# print(order_df.loc[:, "quantity"].mode())
# print(order_df.loc[:, "price"].mode())
# print(order_df.loc[:, "freight_value"].mode())
# print(order_df.loc[:, "product_weight_gram"].mode())