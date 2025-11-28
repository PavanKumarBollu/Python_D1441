"""
Working with csv files
CSV
---
Comma separated values


Csv file all the values are separated by comma

how to read the csv file in python
    1. read the file which is in same location
    2. read the file which is in different location

"""

"""

1. read the file which is in same location

reading the file which is present in same location means we are tring to read the csv file in a python file and both files
are present inside a same folder
for example if the csv file is present inside a folder called readcsv then the python file should present inside the same file


if both are present in the same location we don't need to tell the full path 
we can simply mention the file name that is enough for reading the csv file

"""

# import pandas as pd
#
# data = pd.read_csv("customer_data.csv")
# print(data)


"""
2. read the file which is in different location
if both are present in the different location we need to tell the full path 
we can simply copy the file path and mention the file name that is enough for reading the csv file


"""

# import pandas as pd

# data = pd.read_csv("C:\\Users\\bpava\\Desktop\\student_data.csv")
# print(data)


# read the csv file which is separated by ; not with ,


# data1 = pd.read_csv("salesdata.csv", sep=";")
# print(data1)



# import pandas as pd

# data = pd.read_csv("customer_data.csv", sep=",", header="infer")# heder is nothing but where the columns heading present and whern you say infer it will finds out automatically
# print(data)
# print(data.head())
# print(data.head(10))# to read the top 10 records
# print(data.head(20))# to read the top 20 records

# print(data.iloc[10:20])
# print(data.tail())
# print(data.tail(7))
# print(data.tail(10))


# read the 101 record
# print(data.iloc[101]) # reading the particulate record




"""
writing the data to the csv file
    write in the same location 
    write in the different location

to write the data to a csv file then we can use the to_csv function


"""
# write in same location and different location
import pandas as pd

student_data = {

    "name":["PK"],
    "Age":[25],
    "Gender":["Male"],
    "phoneNo":[1234567899],
    "email":["abc@gmail.com"],
}

df = pd.DataFrame(student_data, columns=["name","Age","Gender","phoneNo","email"])
file_name = "student_details1441.csv"
file_name1 = "C:\\Users\\bpava\\Desktop\\student_details1441.csv"

df.to_csv(file_name, index=False)
df.to_csv(file_name1,index=False)

