"""
updating the column name
updating the records values
or converting the thing into lowercase or upper case

"""
import pandas as pd

students_data = {

"Name":["Pavan","AMB","AA"],
"Age":[50,51,55],
"Qualification":["msc", "b-tech", "a-tech"]

}

# updating the column name
# to update the column name we will use the rename function as shown below

df = pd.DataFrame(students_data)
print(df)

df = df.rename(columns={"Age":"AsOfDOB"})

print(df)


# updating the records values

# update the 2 nd record qualification to Degree instead of b-tech
print(df.loc[1])

df.loc[1] = ["AMB", 51, "Degree"]
print(df)

# convert the column names into lowercase or uppercase
# to do the above we will use the columns for getting the all columns


df.columns = df.columns.str.lower()
print(df)