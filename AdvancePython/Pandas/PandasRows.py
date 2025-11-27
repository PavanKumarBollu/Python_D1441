# inserting a new row(record)
# to insert the new records into the dataframe we will use the concat function
# this function will insert the new record at the last of the dataframe

# df.concat(objects) --> here the objects can be a Series or Dataframe
import pandas as pd

students_data = {
"Name":["Pavan","AMB","AA"],
"Age":[50,51,55],
"Qualification":["msc", "b-tech", "a-tech"]
}

df = pd.DataFrame(students_data)
# print(df)

names = ["Name","Age","Qualification"]
values = ["Kumar", 30, "MSC"]
series = pd.Series(values, index=names)
# print(series)
# df = pd.concat([df,series.to_frame().T], ignore_index=True)
df.loc[len(df)] = series
# print(df)


# inserting multiple rows (records)

multi_rows = [
    {"Name":"abc","Age":25,"Qualification":"m-Tech"   },
    {"Name":"def","Age":36,"Qualification":  "PHD"  },
    {"Name":"ghi","Age":37,"Qualification": "m-phil"  } ]


new_rows_df = pd.DataFrame(multi_rows)

df = pd.concat([df,new_rows_df], ignore_index=True)
print(df)




# new_rows_df = pd.DataFrame([{"Name":"abc","Age":25,"Qualification":"m-Tech"   },
#     {"Name":"def","Age":36,"Qualification":  "PHD"  },
#     {"Name":"ghi","Age":37,"Qualification": "m-phil"  }])
# df = pd.concat([df,new_rows_df], ignore_index=True)
# print(df)



# df = pd.concat([df,pd.DataFrame([{"Name":"abc","Age":25,"Qualification":"m-Tech"   },
#     {"Name":"def","Age":36,"Qualification":  "PHD"  },
#     {"Name":"ghi","Age":37,"Qualification": "m-phil"  }])], ignore_index=True)
# print(df)


# adding a new row at specified locations
# to insert a new record at specified location we will use the .loc function
# dataframe.loc(row label, column labels[optional])

record_to_insert = {"Name": "Sb", "Age": 30, "Qualification": "PHD" }

row_index_to_insert = 3.4 # this will work like after 3rd record only it should insert any value betwenn 3 -4 for inserting after the 3rd record
df.loc[row_index_to_insert] = record_to_insert
df = df.sort_index().reset_index(drop=True)
print(df)


