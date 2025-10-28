"""
Functions are reusable block of code that can perform some specific task

functions allows us the group the logic and makes it easier to use when ever we want

when you want to test the functionality with different input then the functions are best suited


function syntax :
-----------------

def function_name(parameters):
    #lines of code (function body)
    return (optional)

def --> this is a keyword which indicates to the compiler that we are creating a function


function_name --> name of the functino which you are gonna use throught the program

parameters --> parameters are temporory variables which are used to store the input values inside the function
parameters don't have the life outside the function (we can't use the parmeters outside the function body)


functioon_body --> the logic which you want to write inside the function so that when ever we use the function name
automatically this logic will execute

return --> this is a optional statement which is used to return the result in some cases after performing some
calculations

parameters vs arguments
parameters are the placeholder which are used inside the funciton defination where are the argumetns are actual values
which are passed to the fucntions


abstraction -->  which means we don't see the internal logic of the function but we will use it in our program


"""


# def add(num_1, num_2):
#     print(num_1 + num_2)
#
#
# # print(num_1 + num_2) # since the num_1 , num_2 are the parameters they are not accessble outside the add function
#
# # add(1,2)
#
# add(3,4)#7 3, 4 are called arguments
# add(-5, -10)#-15
# add(12,13)#25



# def welcome_msg(user_name, message = "Anudip"):
#     if user_name != " ":
#         print(f"{user_name } Welcome to {message}")
#
#
#
# # use the welcome_msg function to welcome the anudip students
#
# u_name = input("What is your name? : ")
#
# welcome_msg(u_name, "Anudip Family")
#
# # use the welcom _msg function to welcom to DAnlc batch
#
# welcome_msg(u_name, "DANLC Batch ")
# welcome_msg(u_name)


"""
types of functions in python
----------------------------
in programming laguage like python we will have two types of functions 
    1. in-built functions
    2. user-defined functions
    
1. inbuilt functions
    the funciton which are already available in python programming language that function we will call it as in-built
    functions
    like print() input() int() float() list() tuple() min() max() len() open() read() write() keys() values()
    append() push() pop() ...etc

2. user-defined functions:
    the functions which are defined by the programmer(user) we will call it as a user-defined functions
    examples : add() subtract() mul() div() square() find_large() check_eligibility() 
    large_of_three_num() ...etc 



"""





