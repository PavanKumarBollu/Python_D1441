"""
Conditional Statements ( if elif else)

as a python programmer we always wanted to decide what should happen the program like controlling the program
to control the program we need to tell what exactly we wanted to happen like
Ex: when user is more than 18 years old then only allow him to vote other wise tell him to wait for age of 18 years
like above if we want to do something in the programming then we need the help of the conditional statements

Conditional statements are used to check or apply some condition in order to get what we are expecting
in conditional statements we have the following to write the conditions

if
elif
else
by combining all the above we can archive anything we want

if condition
------------


when you want to use something which is already available in programming then we need to follow some rule that rules only
we call it as syntax :

if Syntax:
----------

if condition:
    #lines of code to be executed when the condition is true


#when the above condition is not true then it will skips all the lines inside the if condition






"""

#
# age = int(input("Enter Your Age: "))
# if age < 18: # assume the user is entered the value as 20 then it will be like 20 < 18 --> False then no code inside the if will be executed
#     print("You are young.")


# take the input from user then check weather the user is eligible to vote or not
# the condition for voting is the user age should be 18 or more than 18 years old

# user_age = int(input("Enter your age: "))

"""
if else
-------
if condition:
    #lines of code to be executed when the condition is true
else:
    #lines of code to be executed when the condition is not true(False)


"""

# if user_age >= 18:
#     print("User is eligible to vote ")
# else:
#     print("User is not eligible to vote ")



"""
when you have more than one condition to check then we have to use the elif in the condition to check more tha one condition
if condition_1:
    #lines of code to be executed when the condition is true
elif condition_2:
    #lines of code to be executed when the condition is true
else:
    #lines of code to be executed when the condition is not true(False)

"""

# user_age = int(input("Enter your age: "))
#
# if user_age >= 18:
#     print("User is eligible to vote ")
# elif user_age < 1:
#     print("User is just born baby or not born at all how come he will vote")
# else:
#     print("User is not eligible to vote ")


# user_age = int(input("Enter your age: "))
#
# if user_age >= 18 and user_age <= 65:
#     print("User is eligible to vote ")
# elif user_age < 1:
#     print("User is just born baby or not born at all how come he will vote")
# elif user_age > 100:
#     print("user is form another planet so he will live forever")
# else:
#     print("User is not eligible to vote ")




#task to do in 15 minutes
"""
take the input form the user like age
according to the age do the following
if age between 1- 18 then display young
if age between 19 - 30  then display adult
if age between 31 - 50 then display post adult
if age between 51 - 75 then display old
if age between 75 - 100 then display pretty old
apart form the above condition mention please enter valid age 

"""











