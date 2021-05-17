import pandas as pd

# File CSV
df_csv = pd.read_csv("./datasets/sample_csv.csv")
print(df_csv.head(3)) # Menampilkan 3 data teratas

# File TSV
df_tsv = pd.read_csv("./datasets/sample_tsv.tsv", sep='\t')
print(df_tsv.head(3)) # Menampilkan 3 data teratas

# File xlsx dengan data di sheet "test"
df_excel = pd.read_excel("./datasets/sample_excel.xlsx", sheet_name="test")
print(df_excel.head(4)) # Menampilkan 4 data teratas

# File JSON
url = "./datasets/covid2019-api-herokuapp-v2.json"
df_json = pd.read_json(url)
print(df_json.head(10)) # Menampilkan 10 data teratas