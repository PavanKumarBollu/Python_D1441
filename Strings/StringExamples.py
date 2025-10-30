# # take the input from the user and count the vowels in the given input
#
# u_input = input("Enter your string here :")
# print(f"user entered values is {u_input}")
#
# u_input = u_input.lower()
# print(f"converted into lowecase is {u_input}")
#
# vowels_count = 0
#
# for char in u_input:
#     if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
#         vowels_count += 1
#
# print(f"vowels count is {vowels_count}")
#
# """
# input --> The Qucik FOX Jump Overs tHe Lazy dOG
#
# output count  --> 10
#
# """


# take the input form the user and reverse it use for loop in the logic

# u_input = input("Enter your string here :")
#

# reversed_string = ""
#
# for char in u_input:
#     reversed_string = char + reversed_string
#
#
# print(reversed_string)
#
#
# """
# input = ABCD
#
# reversed_string = ""
#
# 1 st iterations :-
# char = A
# reversed_string = char + reversed_string --> A + "" --> A
#
# 2nd iterations :-
# char = B
# reversed_string = char + reversed_string --> B + "A" --> BA
#
# 3rd iterations :-
# char = C
# reversed_string = char + reversed_string --> C + "BA" --> CBA
#
# 4th iterations :-
# char = D
# reversed_string = char + reversed_string --> D + "CBA" --> DCBA
#
# output = DCBA
#
#
# """

# u_input = input("Enter your string here :")
#
# result=""
# length_of_string = len(u_input)
#
# while length_of_string > 0:
#     result += u_input[length_of_string - 1]
#     length_of_string -= 1
#
# print(result)
#



# take the input from the user and count the charecters and digits and display the count

# u_input = input("Enter your string here :")
#
# char_count = 0
# digit_count = 0
#
# for char in u_input:
#     if char.isdigit():
#         digit_count += 1
#     elif char.isalpha():
#         char_count += 1
#
# print(char_count, digit_count)
#
#
# """
# input = Madhpur@500081
# output =    chars --> 7
#             digits --> 6
# """

# take the input from the user and display the  characters and digits separately

#
# u_input = input("Enter your string here :")
#
#
# chars = ''
# digits = ''
#
# for char in u_input:
#     if char.isdigit():
#         digits += char
#     elif char.isalpha():
#         chars += char
#
# print(chars)
# print(digits)
#
# """
# input = 144DANLC1
# output =
# DANLC
# 1441
#
# """







