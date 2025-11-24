u_input = input("enter the string here : ")

# Example : KAsHifa
# K --> 75 --> 75 + 32 --> 107 --> k
# A --> 65 --> 65 + 32 --> 97 --> a
# s --> s
# H --> 72 --> 72 + 32 --> 104 --> h
# i --> i
# f --> i
# a --> a

# to lower case
def convert_lowercase(u_input):
    result = []
    for char in u_input:
        if "a" <= char <= "z":
            # print(char)
            result.append(char)
        elif "A" <= char <= "Z":
            print(ord(char))
            code_char = ord(char)
            code_char += 32
            lowercase_char = chr(code_char)
            result.append(lowercase_char)
            # print(lowercase_char)
        elif char == " ":
            result.append(" ")
        else:
            print("Something went wrong")
    return "".join(result)


results = convert_lowercase(u_input)
print(f"the lower case String is: {results}")








# to Upper case
# to capitalize each starting letter


