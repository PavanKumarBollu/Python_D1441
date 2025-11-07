# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# t1 = (1,2,3,4,5,6,7,8,9,10)

# print(t1[::-1])#


#set datastructure 
"""
set is a collection of elements in python the the order not preserved 

set will store unique elements only (no duplicate values)
features of set 
---------------
unordered 
mutable
duplicates are not allowed 
no-indexing 

"""
#Creating the sets
# set_num = {1,2,1,2,3,5,4,-1,0,"pavan"}
# print(set_num)


#creating the set from the list
# list_nums = [10,12,21,34,21,10,11,12,100,99,120,34,45,45,12]
# print(list_nums)

# set_nums_list = set(list_nums)
# print(set_nums_list)


#creating the empty set
# empty_set = {}
# empty_set_const = set()

# name = "pavan"
# name_without_duplicates = set(name)
# print(name)
# print(name_without_duplicates)


# person_set = {"PK",54,6.0, "Tollywood", "AP", 'SRK',"MB","AA"}
# print(person_set)

# person_set.add(1234567891)
# print(person_set)

# person_set.remove("SRK")
# print(person_set)

# person_set.discard("SRKs")
# print(person_set)

# person_set.clear()
# print(person_set)

# set_1 = {1,2,3}
# set_2 = {4,2,5}
# union is used to get the unique elements from the both list if the element is repeated then also it will considers only once
# set_3 = set_1.union(set_2)
# print(set_3)

#intersection is used to get the common elements form the both sets
# set_4 = set_1.intersection(set_2)
# print(set_4)

set_5 = {1,2,3,4,5,6,7,8,9,10}
set_6 = {6,7,8,9}

print(set_6.issubset(set_5))#True
print(set_5.issubset(set_6))#False

print(set_6.issuperset(set_5))#False
print(set_5.issuperset(set_6))#True



































