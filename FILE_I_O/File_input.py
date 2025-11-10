"""
Data_Persistence
persistence is nothing but store data into a permanent location(files) and use that data later point of view

the permanent location means saving the data into a files or to a database


files --> data will be stored in the same system inside the storage device
databases --> data will be stored in the database server and this data can be retried across multiple systems

"""
"""
working with the files
----------------------


working with the files in the sense we need to read the data from the file or we need to write something into that file
read()
write()

reading the data from a file
----------------------------
reading the data from a file in the sense we will read the contents inside that files like what exactly it contains then 
we can work with data inside of it
to read the data from a file we will use the open() function to open the file then we will say what we are goonna do with 
that file

"""
# when you have the python file and file that you would want to open in the same folder just mention the file name
# no need to mention the file location fully
file_read = open("data.txt","r")

if file_read:
    print(file_read.read())



# when you have the python file and file that you would want to open in different location(different folder)
# then you need to mention the full path of the file which you want to open()

file_different_loc = open("C:\\Users\\bpava\\Downloads\\123.txt", "r")

if file_different_loc:
    print(file_different_loc.read())











