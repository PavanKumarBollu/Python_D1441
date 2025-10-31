"""
List
----

for example we have 5 student names and we want to work with the student name in rugular datatype we will use like following
std_1 = 'PK'
std_2 = "SMB"
std_3 = "JK"
std_4 = "KL"
std_5 = "MK"


when in above case it is very difficult to maintain the student name as it is only 5 names we can try to create separate
variables but what if we have 100 student names we can't create 100 variables in the program
like this if you have 1000 student names to store in the program then we need some more advanced datatype to handle this
type of data

in python to handle this kind of senarios we have advanced data structrues like list tuple set dictionary ...etc




"""

std_1 = 'PK'
std_2 = "SMB"
std_3 = "JK"
std_4 = "KL"
std_5 = "MK"

# to store all the above values in a list we will do the following

# student_names = ['PK', 'SMB', 'JK', 'KL', 'MK']
# print(student_names)



"""
--> list is a ordered Ds that means the order which we are storing elements will be remembered 
--> mutable -- we can modify the list like we can update any value or we can add some more values(elements)
--> heterogeneous data --> we can store mixed types of elements inside a single list example we store text , numers in a single list
--> dynamic in size --> list is not fixed with any size we can store any number of elements as we want
"""

# examples

# list_std = ["PK", 25 , 5.9 , True, False, 'Madhapur']
# print(list_std)
#



# accessing the elements of the list
# list is a zero based index exactly like string
# list_std = ["PK", 25 , 5.9 , True, False, 'Madhapur']
# print(list_std)
# print(type(list_std))
# print(len(list_std))
#
#
# #slicing
# print(list_std[0])
# print(list_std[-1])
#
# print(list_std[::])
# print(list_std[:3])
# print(list_std[3:5])
# print(list_std[::-1])

#append() function is used to append new element at last position
# list_std = ["PK", 25 , 5.9 , True, False, 'Madhapur']
# print(list_std)
# list_std.append('HYD')
# list_std.append(102.32)
# print(list_std)

# list_std = ["PK", 25 , 5.9 , True, False, 'Madhapur']
# list_subName = ["maths", "physics", "chemistry"]
#
# list_std.extend(list_subName)
# print(list_std)



#insert an element at specified location we can do this by using the insert() function
# list_std = ["PK", 25 , 5.9 , True, False, 'Madhapur']
# print(list_std)
# list_std.insert(1,"SMB")
# print(list_std)


#remove will take the actual value to remove form the list where as the pop will take the index value and removes the element
# list_std = ["PK", 25 , 5.9 , True, False, 'Madhapur']
# print(list_std)
#
# list_std.remove('Madhapur')
# print(list_std)
#
# list_std.pop(1)
# print(list_std)


#
# scores =  [40,50,60,70,80,90,45,55,66,77,88,46,42,43,44,47,78,87,98,99]
#
# for p in scores:
#     if p % 2 == 0:
#         print(p)#prints each score in a line
#
#
# num = 0
# while num < len(scores):
#     if scores[num] % 2 == 0:
#         print(scores[num])
#
#     num += 1






