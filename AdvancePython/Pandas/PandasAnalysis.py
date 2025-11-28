import pandas as pd

data = pd.read_csv("customer_data.csv")
# print(data.describe())
# print(data.info())

# print(data["Age"].value_counts(sort=True, dropna=True,ascending=False))

# data_no_na = data.dropna(how="all", inplace=False)
# print(data_no_na)

data_duplicated = data.duplicated()
# print(data_duplicated)
# print(f"total duplicated records count {len(data[data_duplicated])}")
# print(len(data))
#
# data = data.drop_duplicates()
# print(len(data))

# print(data[data_duplicated]) # to print only the duplicated records

# read the unique values of the column
# print(data["State_names"].unique())
# print(data["Gender"].unique())



# print(data.sort_values(by="Amount_spent").head(50))
# print(data.sort_values(by="Amount_spent", ascending=False).head(50))