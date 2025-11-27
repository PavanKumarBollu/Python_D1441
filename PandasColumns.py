import pandas as pd

students_data = {
"names":["Pavan","AMB","AA"],
"Age":[50,51,55],
"Qalification":["msc", "b-tech", "a-tech"]
}

df = pd.DataFrame(students_data)
print(df)

#Insert into the dataframe

# Inserting a column
df["Place"] = ["HYD", "BNGL", "Mumbai"]
print(df)




# inserting multiple columns
new_columns = {
    "Marks": [50,55,56],
    "Gender": ["Male", "Female", "Male"]
}

df["Marks"] = new_columns["Marks"]
df["Gender"] = new_columns["Gender"]

print(df)


#inserting a new column at wanted location
# for inserting a new column at specified location we will use the insert function
# df.insert(location, columnName, values)

mobileNumber = [123456,654789,365478]

df.insert(2,"MobileNumber",mobileNumber) # note location values will starts from 0 not from 1 if you want to inset in 2 position then say 1
print(df)

# for i in range(3):
#     df.insert(i, f"MobileNumber{i}", mobileNumber)
# print(df)
#
