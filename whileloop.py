"""
while statement is a control flow statement in python and that is used for controlling the flow of execution
and allows us to execute the logic repeatedly.

while syntax :

while condition:
    #code to be executed while the mentioned condition is true
    increment / decrement


"""

# while examples

# count = 1
#
# while count <= 25:
#     if count % 2 == 0:
#         print(count)
#     count += 1

#



# count = 1
# while count < 100:
#     count += 1
#     print(count)
#     if count == 30:
#         break # used for breaking the loop and coming out
#


# print the even number form a range like 10 - 150 or something else take the input from the user

num_start = int(input("Enter the start number: "))
num_end = int(input("Enter the end number: "))

while num_start < num_end:
    if num_start % 2 == 0:
        print(num_start)
        num_start += 1
    else:
        num_start += 1
        continue #skips the current execution then go for the next iteration







# while True:
#     print("DANLC")