import pandas as pd

# Baca file sample_csv.csv
df = pd.read_csv("./datasets/sample_csv.csv")
# Slice langsung berdasarkan kolom
df_slice = df.loc[(df["customer_id"] == "18055") &
(df["product_id"].isin(["P0029","P0040","P0041","P0116","P0117"]))
]
print("Slice langsung berdasarkan kolom:\n", df_slice)

# Set index dari df sesuai instruksi
df = df.set_index(["order_date","order_id","product_id"])
# Slice sesuai intruksi
df_slice = df.loc[("2019-01-01",1612339,["P2154","P2159"]),:]
print("Slice df:\n", df_slice)