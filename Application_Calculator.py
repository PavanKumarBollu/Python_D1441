"""
take the input from the user and accroding to the user need do the calculation then display the result
give the user bunch of options to choose then accordingly act
example if user say 1 then do the addition
if user say 2 then subtract 2
if user say 3 then multiply
if user say 4 then division
if user say 5 or any other wrong input the exit (quit) form the application


"""
while True:
    print("Choose any of the following options: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print()
    choice = int(input("Enter your choice here : "))

    if choice == 1:
        num_1 = int(input("Enter first number : "))
        num_2 = int(input("Enter second number : "))
        print("The result is: ", num_1 + num_2)
    elif choice == 2:
        num_1 = int(input("Enter first number : "))
        num_2 = int(input("Enter second number : "))
        print("The result is: ", num_1 - num_2)
    elif choice == 3:
        num_1 = int(input("Enter first number : "))
        num_2 = int(input("Enter second number : "))
        print("The result is: ", num_1 * num_2)
    elif choice == 4:
        num_1 = int(input("Enter first number : "))
        num_2 = int(input("Enter second number : "))
        print("The result is: ", num_1 / num_2)
    else:
        break




