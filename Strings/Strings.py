
"""
Strings
-------

string is a collection characters (a-z, A-Z, 0-9, symbols( @#$%^&*(! ))

String is a built-in data type in python which is used to store any type of value

String are always mentioned inside the quotations only
we can mention anything form the keyboard but it should be in the quotations

"""

# name  = "PK"
# print(name)
# print("PK")
#
# address = 'Madhapur it\'s '
# address2 = "it's in madhapur "
#
# address_2 = """ Ayyapa socity
# madhapur
# hyderabad
# telangana
# """
# # when you want to create the string in multiple lines then use the threple quotes
# print(name)
# print(address)
# print(address_2)
# print(address_2)
#
# email = "abc123@gmail.com"
# password = "BPKY@123$HYD"
# print(type(email))
# ifsc_code = "UBIN0408174"
# ration = "1:3"
# percentage = "20%"
#
#
# """
# Note : Anything you collect from the user in your program then that will come to us in the form of string only
# but later we can convert that into specify type as we wanted
#
# """



# accessing the individual characters

# str = "Anudip Madhapur"
# in string each charecter have been given a number which we call it as index starting from 0
# example in the above case the value of Anudip Madhapur will be given the index like the following
"""
A --> 0
n --> 1
u --> 2
d --> 3
i --> 4
p --> 5
  --> 6 # here space is also counted in the strings
M --> 7
a --> 8
d --> 9
h --> 10
a --> 11
p --> 12 
u --> 13
r --> 14

"""

# print(str)
# print(str[7]) # prints M to the console
# print(str[6])
# print(str[8])



#length function
# print(len(str)) # counts the total characters in the string and prints the number to the console


#Slicing

# if you want to extract some portion of the string we can do the following
# print(str[1:5]) #[start:end] always we need to mention the end value+ 1 because the internal logic will be considered
#     #till end -1 value for example if you want the values till 8 th position then we need to mention 8+1 => 9

# str = "Anudip Madhapur"
# print(str)
# print(str[::]) # print(str[::]) == print(str) when you are not mentioning the start and end value default values will
# be considered the default values of the start = 0 and end = len(str)


#print each alternative characters form the given string
# input = "Anudip Madhapur"
# output = "Aui ahpr"

# print(str[::2]) #[start:end:step-up value] step up value is nothing but the gap between the current character and next character


# take the input from the user then reverse it
#
# u_input = input("Enter Anything here to reverse it : ")
#
# print(u_input[::-1]) # -1 we call it as negative  indexing

"""
A --> -15
n --> -14
u --> -13
d --> -12
i --> -11
p --> -10
  --> -9 # here space is also counted in the strings
M --> -8
a --> -7
d --> -6
h --> -5
a --> -4
p --> -3 
u --> -2
r --> -1

"""
# print(str[-1]) # -1 --> r
# print(str[len(str)-1])#14 --> r











