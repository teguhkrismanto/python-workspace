import pandas as pd
import matplotlib.pyplot as plt

order_df = pd.read_csv("./datasets/order.csv")

# The median price paid by the customer for each payment method
median_price = order_df["price"].groupby(order_df["payment_type"]).median()
print(median_price)

# Change freight_value to shipping_cost and find the most expensive shipping_cost from the sales data using sort
order_df.rename(columns={"freight_value": "shipping_cost"}, inplace=True)
sort_value = order_df.sort_values(by="shipping_cost", ascending=0)
print(sort_value)

# For product_category_name, what is the average weight of the product and which standard deviation is the smallest from that weight
mean_value = order_df["product_weight_gram"].groupby(order_df["product_category_name"]).mean()
print(mean_value.sort_values())

std_value = order_df["product_weight_gram"].groupby(order_df["product_category_name"]).std()
print(std_value.sort_values())

# Create a sales quantity histogram from the dataset to see the distribution of the sales quantity with bins = 5 and figsize = (4,5)
order_df[["quantity"]].hist(figsize=(4, 5), bins=5)
plt.show()