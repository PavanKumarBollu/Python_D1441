"""
Dictionary
----------
word :  definition of the word


dictionary is a built-in ds in python which will help us to store the values with the help of key
in general dictionary is nothing but key:value pairs

key : value

dictionary is unordered means no order is maintained
dictionary is mutable means we can modify the dictionary at any point of time in the program
its dynamic means size is not fixed
we can access the values by using the keys
best performance in terms of lookup
we can't duplicate the keys
we can iterate over the dictionary

"""
person = {
    "name":"PK",
    "age":22,
    "friends":['PKS', "BPK"]
}
#
# print(person)
# print(type(person))

# name , age , friends is the keys and "PK", 22 ['PKS', "BPK"] is the values


# common uses of the dictionary
# storing the configuration settings of any application...etc
# product information
# profile settings
# storing the information with some labels
# storing the items availability of the stores with the help of the product name

# attendance
# students = {
#     "pk":["P","A","L","P","A"],
#     "BPK":["P","A","L","P","A"]
# }

#creating the dictionary

#empty dictionary
empty_dict = {}

#creating the dictionary with some key values

dict_with_key_values = {
    "name":"PK",
    "age":22,
    "friends":['PKS', "BPK"],
    "height":5.78
}

#using the dict() constructor

empty_dict = dict()
dict_constructor_with_key_values = dict(name="PK", age=22, height=5.78)

print(dict_constructor_with_key_values)




















