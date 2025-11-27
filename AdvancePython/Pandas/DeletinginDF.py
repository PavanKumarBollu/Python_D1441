"""
to delete a column which not required anymore we will use the drop function

"""

import pandas as pd

students_data = {

"Name":["Pavan","AMB","AA"],
"Age":[50,51,55],
"Qualification":["msc", "b-tech", "a-tech"]

}

df = pd.DataFrame(students_data)

print(df)

df = df.drop('Age', axis=1)
print(df)


# deleting the rows
df = df[df["Name"] != "Pavan"]
print(df)