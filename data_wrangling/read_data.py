import pandas as pd

csv_data = pd.read_csv("https://storage.googleapis.com/dqlab-dataset/shopping_data.csv")

# display all data
print (csv_data)

# display first 5 data by default
# head(n) display first n data
# print (csv_data.head())

# display last 5 data by default
# tail(n) display last n data
# print (csv_data.tail())

# display row x column
# print(csv_data.shape)

# display only specific column('Age')
# print (csv_data['Age'])

# display data at row 5
# print(csv_data.iloc[5])

# display specific column('Age') at row 1
# print(csv_data['Age'].iloc[1])

# display data from row 5 to 9
# print(csv_data.iloc[5:10])

# display basic statistic from each column such as count, unique, top, freq, mean, std, min, 25%, 50%, 75%, max. include NaN values
# print(csv_data.describe(include='all'))

# display basic statistic from column whom contains numerical values
# print(csv_data.describe(exclude=['O']))