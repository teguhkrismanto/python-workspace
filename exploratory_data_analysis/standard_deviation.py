import pandas as pd

order_df = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/order.csv")

# Standar deviation of product_weight_gram
standar_deviation = order_df.loc[:, "product_weight_gram"].std()
print(standar_deviation)

# Varians of product_weight_gram
varians = order_df.loc[:, "product_weight_gram"].var()
print(varians)