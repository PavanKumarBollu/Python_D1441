"""
control Statements (for while)
------------------------------

when you want to some activity repeadly for certain number of times or until the user says quit then we need the help of
control statements


control statements are used to control the flow of the program

in control statements in python we have two types
    1. for loop --> when we know the repetation count then for loop
    2. while loop --> when we don't know the repetation count then while loop

"""


"""
1.  for loop

for loop is a statement in python which is used to execute some logic repeatedly for certain number of times
for certains number of times means like 10 time 20 time or 50 time ...... n number of times

basically for loop is used to loop over a sequence like list or String or arrays ...etc


syntax :

for variable in sequence:
    # lines of code to be executed for n times

when you say last value mention lastvalue + 1 becuase the loop will run for lastvalue - 1 times only
"""
#examples of for loop
#print numbers from 1 to 10

# for i in range(1, 11):
#     print(i) #prints the numbers form 1 to 10
#     # print("Pavan")

# print the even numbers from 0 to 100

# for i in range(0,101):
#     if i % 2 == 0:
#         print(i)

#print the odd numbers form 0 to 100
# for i in range(0, 101):
#     if i % 2 != 0:
#         print(i)


# print the 2 table
# num = 2
# for i in range(1, 11): # i is a variable and it can be any name like pavan or j or anything
#     print(f"{num} x {i} = {num * i}")
#     # print(num * i)


"""
nesting for loop 

writing a for inside an other for loop is called nesting of the loops
by writing the nested loop we can archive the complex things easyly

nested for loop syntax

for outer_variable in sequence:
    # outer loop lines of code
    for inner_variable in outer_variable:
        #inner loop lines of code
    # rest of the outer loop lines of code
    

"""

# for i in range (1,5):
#     for j in range (1,11):
#         print("*",end=" ")
#     print()

# for i in range(1,7):
#     for j in range(0, i): # i = 1, i = 2 ... i = 6
#         print("*", end=" ")
#     print()


# take the number from the user then display the pyramid style

# num = int(input("enter the number : "))
#
# for i in range(1, num + 1):
#     print(" " * (num - i), end=" ")
#     print("* " * i)









