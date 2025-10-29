
# iterate through each character
str = "Accenture Madhapur" # 18 charecter
# print(len(str))

# for char in str:
#     print(char)

# count = 0

# while count < len(str):
#     print(str[count])
#     count += 1

# str_1 = "Pavan"
# str_2 = "Kumar"
#
# # + can be used to add to string and here + is called as concatenation operator
# str_full = str_1 + " " + str_2
# print(str_full)
#


# str_3 = "PK"
# print(str_3 * 3)

""" 
note: we can use all the comparision operators to compare the strings like 
== != > < >= <= 
"""
# String Formatting
# ----------------

""" 
in python we can format the string using the place holders at runtime when the program is executing by the compiler 
that place holders will be replaced with orginal values 
--> in python we can format the string by using %s  or .format() function

"""

#using the % symbol to format the string
# name = "AA"
# age = 45
# print("The name of the start is %s , and age is %d years old ."%(name,age))
#
#
# name = "NTR"
# age = 47
# print("The name of the start is %s , and age is %d years old ."%(name,age))
#

name = "NTR"
age = 47

print("My name is %s and i am %d years old ."%(name,age))
print("My name is {} and i am {} years old".format(name, age))
print(f"My name is {name} and i am {age} years old")








