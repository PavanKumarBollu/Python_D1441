"""
to perform some calculations we need help that help we will get from the operators

Operator --> it is a simbol which has some predefined meaning and helps us to do some basic calculations
Operand  --> the actaul values which are involved in operations
Examples
a - b
10 + 20

here a ,  b are operands
10 ,20 are also operands
where are + , - are operators


"""

"""Types of operators are:
 Arithmetic Operators: -
    addition +
    subtraction -
    multiplication *
    division /
    modulo %
    exponentiation **
    floor division //
    
 comparison operators: -
    Equality operator: ==
    Not Equality operator: !=
    less than < 
    greater than > 
    less than or equal to <=
    greater than or equal to >= 
 
    
 logical Operators:
        and 
        or 
        not 
 assignment operators :
    equals =
    +=
    -=
    *=
    /=
    %=
    **=
 membership operators:
    in
    not in
    
 Identity 
    is
    is not (negated identity)
 
 bitwise operators
    & bitwise and
    | bitwise  or
    >> right shift
    << left shift
    ^ XOR
    ~ NOT
 
 Ternary Operator : 
 
"""

# Arithmetic Operators: -

# a = 10
# b = 20
#
#
#     # addition +
# print(a + b) # 30
#
#     # subtraction -
# print(a - b) #-10
#
#     # multiplication *
# print(a * b) #200
#
#     # division /
# print(a / b) # 0.5
#
#     # modulo %
# print(a % b) # 10
# print(12 % 24) # 12
# print( 20 % 12) # 8
# print( 18 % 12) # 6
# print( 16 % 3) # 1
#
#     # exponentiation **
# print(a ** b) # 100000000000000000000
#
#     # floor division //
# print(a // b) # 0
#


# comparison operators: -
# when you use the comparison operators then the result will always True or False only
#
# print("comparison operators")
    # Equality operator: ==
# == operator is used to check weather the two values are same or not if same then true otherwise false
# name_1 = "PK"
# name_2 = "PK"
#
# print(name_1 == name_2) #True
# name_2 = "BPK"
#
# print(name_1 == name_2) #False



    # Not Equality operator: !=
# when you want to check weather the two values are not same then we can use the != operator
# name_1 = "PK"
# name_2 = "PK"
#
# print(name_1 != name_2) #False
# name_2= "BPK"
# print(name_1 != name_2) #True
#
#     # less than <
# num_1 = 20
# num_2 = 25
# print(num_1 < num_2)#True
#
#
#     # greater than >
# print(num_1 > num_2)#Fasle
#
#
#     # less than or equal to <=
# num_3 = 30
# num_4 = 30
#
# print(num_3 <= num_4) #True
#
# num_4 = 29
# print(num_3 <= num_4) #False
#
#
#     # greater than or equal to >=
#
# num_3 = 30
# num_4 = 30
# print(num_3 >= num_4) #True
#
# num_4 = 31
# print(num_3 >= num_4) #False

# logical Operators:
#         and
# num_1 = 10
# num_2 = 30
# num_3 = 20

# print(num_2 > num_1 and num_2 > num_3)#True
# print(num_2 < num_1 and num_2 > num_3)#False

"""
print(30>10 and 30>20)
True and True
True
"""



#         or
# print(num_2 > num_1 or num_2 > num_3)#True
# print(num_2 < num_1 or num_2 > num_3)#True
#
# #         not
#
# print(not (num_2 > num_1 or num_2 > num_3))#False
# print(not (num_2 < num_1 and num_2 > num_3))#True


# assignment operators :
# do some activity the assign the value back to same variable

#     equals =
# a = 15
# print(a)#15



#     +=
# a += 10 # a = a + 10 -->  15 + 10 --> 25 --> a = 25
# print(a) #25
#
# b = 123
# b += 2
# print(b) #125

#     -=

# c = 145
# c-=2 # c = c - 2 --> 145-2 --> 143 --> c = 143
# print(c)#143
#
# d = 9876
# d -= 76
# print(d) # 9800


#     *=
# e = 25
# e *= 4
# print(e)#100
#
# f = 210
# f *= 2
# print(f) #420

#     /=
# g = 840
# g /= 2
# print(g) # 420
#
# h = 800
# h /= 8
# print(h) #100



#     %=
# i = 11
# i %= 3
# print(i) #2
#
# j = 125
# j %= 3
# print(j) #2


#     **=
# k = 2
# k **= 10
# print(k) #1024 #512 #256 #128 #64 #32 #16 #8 #4

# membership operators:

# # in
# students_name = ["PK", "SMB","AA","NTR"]
# student_name = "PK"
# print(student_name in students_name)#True
#
# # not in
# student_name_1 = "SRK"
# print(student_name_1 not in students_name) #True



# Identity Operators
# is
# is not (negated identity)

# nums = [1,2,3,4,5]
# nums_1 = nums
#
# print(nums_1 is nums) #True
# print(nums is not nums) #False

# student_name = "PK" #snake_case
# studentName = "PK" #pascleCase
# StudentName = "PK" #CamelCase


# bitwise operators
# & bitwise and


# a = 3
# b = 5
# print(a & b ) #1
# """
# 3 --> 0 0 1 1
# 5 --> 0 1 0 1
# ---------------
#       0 0 0 1
# ---------------
#  0 0 0 1 --> 1
# """

# c = 2
# d = 5
# print(c & d) #0
# """
# 2 --> 0 0 1 0
# 5 --> 0 1 0 1
# ---------------
#       0 0 0 0
# ---------------
#  0 0 0 0 --> 0
# """


# # | bitwise or
# a  = 2
# b = 5
# print(a | b ) #7

# """
# 2 --> 0 0 1 0
# 5 --> 0 1 0 1
# ---------------
#       0 1 1 1
# ---------------
#  0 1 1 1 --> 7
# """


# >> right shift
# print(2 >> 5)#0
#
# # 2 >> 5 --> 2 / 2 ^ 5 --> 2 / 32 --> 0.0625 --> 0
#
# # << left shift
#
# print(2 << 5)#64
#
# # 2 << 5 --> 2 * 2 ^ 5 --> 2 * 32 --> 64
#
# # ^ XOR
# print( 2 ^ 5) #7
# # 2 --> 0 0 1 0
# # 5 --> 0 1 0 1
# # ---------------
# #       0 1 1 1
# # ---------------
# #  0 1 1 1 --> 7





