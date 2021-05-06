import pandas as pd

order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")

# Count quartile 1
q1 = order_df[["product_weight_gram"]].quantile(0.25)
# Count quartile 3
q3 = order_df[["product_weight_gram"]].quantile(0.75)

# Count inter quartile range
inter_quartile_range = q3 - q1
print(q1)
print(q3)
print(inter_quartile_range)