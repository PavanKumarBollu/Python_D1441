
# iterate through each character
# str = "Accenture Madhapur" # 18 charecter
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

# name = "NTR"
# age = 47
#
# print("My name is %s and i am %d years old ."%(name,age))
# print("My name is {} and i am {} years old".format(name, age))
# print(f"My name is {name} and i am {age} years old")
#

# String methods
# sinces String are in-built data types we have some methods(functions) to support us to work with the string
"""
upper()
lower()
capitalize()
strip()
len()
replace()
join()
split()
count()
find()
isdigit()
isalpha()
..
.
.
etc
"""

# str = input("Enter the STring here : ")

# converting everying to upper case
# print(str.upper()) # converts the str to upper case

# convert into lower case
# print(str.lower()) # converts the str to lower case letters


# capitilize the starting letter
# print(str.capitalize()) #capitalizes the starting letter



# print(str.strip()) # removes the white spaces in both sides left and right
# lstrip is used to remove the spaces on the only left side
# rstrip is used to remove the spaces on the only right side

# replace the b character with a

# print(str.replace("b", "a")) # replace will replace the all occurrences of the mentioned characters in the string
# print(str.replace("pavan", "PK"))
# input = pavan is a python trainer pavan teaches the python pavan is always want to teach
# output = PK is a python trainer PK teaches the python PK is always want to teach


# names = ['PK', 'SMB']
#
# print(" ".join(names)) #combines all the values into a string
# print("@".join(names)) #combines all the values into a string

str = input("Enter the STring here : ")

# print(str.split())
# Python Is a Very good programming language to learn but the key to master the python is practice
# ['Python', 'Is', 'a', 'Very', 'good', 'programming', 'language', 'to', 'learn', 'but', 'the', 'key', 'to', 'master', 'the', 'python', 'is', 'practice']


# print(str.count("pavan")) #when you use the count in string it is gonna count the total number of time the particulate charecters repeated


# print(str.isalpha()) # when the total character in the string is alphabets then it will returns true otherwise false
# print(str.isdigit()) # when the total character in the string is numbers then it will return true otherwise false
"""
case 1 
------
input = pavan
output =
True
False

case 2
------
input = 123
output =
False
True

case 3
------
input PavanKumar927
output =
False
False


"""



