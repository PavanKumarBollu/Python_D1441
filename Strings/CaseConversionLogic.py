u_input = input("enter the string here : ")
#
#
# # Example : KAsHifa
# # K --> 75 --> 75 + 32 --> 107 --> k
# # A --> 65 --> 65 + 32 --> 97 --> a
# # s --> s
# # H --> 72 --> 72 + 32 --> 104 --> h
# # i --> i
# # f --> i
# # a --> a
#
# # to lower case
# def convert_lowercase(u_input):
#     result = []
#     for char in u_input:
#         if "a" <= char <= "z":
#             # print(char)
#             result.append(char)
#         elif "A" <= char <= "Z":
#             print(ord(char))
#             code_char = ord(char)
#             code_char += 32
#             lowercase_char = chr(code_char)
#             result.append(lowercase_char)
#             # print(lowercase_char)
#         elif char == " ":
#             result.append(" ")
#         elif 0 <= ord(char) <= 9:
#             result.append(char)
#         else:
#             print("Something went wrong")
#     return "".join(result)
#
#
# results_lower = convert_lowercase(u_input)
# print(f"the lower case String is: {results_lower}")
#
# # to Upper case
#
# # Example : KAsHifa
# # K --> 75 --> K
# # A --> 65 --> A
# # s --> 115 - 32 --> 83 --> S
# # H --> 72 --> H
# # i --> 105 - 32 --> 73 --> I
# # f --> 102 - 32 --> 70 --> F
# # a --> 97 -32 --> 65 --> A
#
#
# def convert_uppercase(u_input):
#     result = []
#     for char in u_input:
#         if "a" <= char <= "z":
#             char_code = ord(char)
#             char_code -= 32
#             result_char = chr(char_code)
#             result.append(result_char)
#         elif "A" <= char <= "Z":
#             result.append(char)
#         elif char == " ":
#             result.append(" ")
#         elif 0 <= ord(char) <= 9:
#             result.append(char)
#         else:
#             print("Something went wrong")
#     return "".join(result)
#
# results_upper = convert_uppercase(u_input)
# print(f"the Upper case String is: {results_upper}")


# to capitalize each starting letter


def capitalize(u_input):
    result = []
    input_list = u_input.split()
    print(input_list)

    for ele in input_list:
        if "A" <= ele[0] <= "Z":
            result.append(ele)

        if "a" <= ele[0] <= "z":
            word_num = ord(ele[0])
            word_num = word_num -32
            char_upper = chr(word_num)
            char_updated = char_upper + ele[1:]

            result.append(char_updated)

    return " ".join(result)




print(capitalize(u_input))


# Task write the logic for the following requirements(remember it will be not a single word)
# input :  PaVaN KuMaR
# result : pAvAn kUmAr


