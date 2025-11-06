my_tuple = (-1,2,3,101,120,10,20,30,40,55,65,75,10,78,90, 100)
# print(my_tuple)

#aceesing the elements
# print(my_tuple[0])# prints the first element of the tuple
# print(my_tuple[1])#prints the second element of the tuple
# print(my_tuple[-1])# prints the last element of the tuple
# print(my_tuple[len(my_tuple)-1])# prints the last element of the tuple


#slicing concept

# print(my_tuple[::])#prints everything of the tuple
# print(my_tuple[::2])#prints each alternative element
# print(my_tuple[4:7])#prints the elements from 4th position to 6th position in total 3 elements
# print(my_tuple[::-1])#prints the tuple in reverse order

#concatination operator
# t1 = (1,2,3)
# t2 = (4,5,6)
# t3 = t1 + t2
# print(t3)

#repeatation operator
# print(t1 * 3)


# membership operator
#
# print(2 in t1)#True
# print(10 in t1) #False
# print(10 not in t1) #True
# print(2 not in t1) #False



#aggregative functions
# print(min(my_tuple))
# print(max(my_tuple))
# print(my_tuple.count(10))# print the total times 10 repeated
#

#Sorting the tuple
# print(my_tuple)
# sorted_tuple = tuple(sorted(my_tuple))
# print(sorted_tuple)



#unpacking means making the tuple elements to store in individual variables
# when you are unpacking the tuple elements then we need to give exact number of variable equals
# to the count of the elements of tuple otherwise too many values to unpack exception(error)
# tuple_t1 = (10,2,3)
# a,b,c = tuple_t1
# print(a)
# print(b)
# print(c)

my_tuple = (-1,2,3,101,120,10,20,30,40,55,65,75,10,78,90, 100)
print(my_tuple)
a ,b, *c , y,z = my_tuple
print(a)
print(b)
print(c)
print(y)
print(z)






# my_tuple = (-1,2,3,101,120,10,20,30,40,55,65,75,10,78,90, 100)


#sum all the tuple values
# sums = 0
# for ele in my_tuple:
#     sums += ele
#
# print(sums)
#
#
# print(sum(my_tuple))

#
# print(my_tuple.index(10))# prints the index number of the first occurrence of the 10 in the in tuple
# print(my_tuple[5])
