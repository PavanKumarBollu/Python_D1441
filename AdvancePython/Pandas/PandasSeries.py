# Pandas basically provides two different data structures to work and manipulate the data
# they are
#     Series
#     DataFrame

#Pandas Series
"""
Pandas Series is like a one dimentional array where each value will be given one index or label to identify the value

to make things very much clear Series is like a single column in the excel where the column contains the values
and each value will be identified by using the index or label
here in padas we can genereate the index automatically or we can use our own labels to identify the values

the values which we can store in the Series DS is any type means we can store any types of data in the series
(float, int, Strings, objects...etc)

"""

# import pandas as pd
#
# marks = [50,60,55,45,60,32,86]
#
# series = pd.Series(marks)
# print(series)
#



import pandas as pd

# semisters
sem_name = ['sem-1','sem-2','sem-3','sem-4','sem-5']

# marks
marks = [55,54,45,66,80]

# creating the series
std_marks = pd.Series(marks, index=sem_name,name="Sem wise student marks comparision")
print(std_marks)
