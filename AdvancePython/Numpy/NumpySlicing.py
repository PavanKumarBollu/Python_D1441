#indexing in numpy
# ni numpy also we can use the indexing concept where each element will be identified with some number
# we can do the negative indexing also possible

import numpy as n

# names = n.array([  'Alice', 'Bob', 'Charlie',])
# print(names)
#
# #access  the first element of the names array
# print(names[0])#gives us the first element of the names array
#
# # access the last element of the names array
#
# print(names[-1]) # gives us the last element of the array
# print(names[len(names)-1]) # gives us the last element of the array
#

#
# num_multi = n.array(
#                     [[1,2,3],#0
#                      #0 1 2 -> index values
#                      [4,5,6],#1
#                      #0 1 2 -> index values
#                      [7,8,9]])#2
#                      #0 1 2 -> index values
#
# #print the element of 2nd row 3rd column of num_multi array which is exactly 6
# print(f"Element at the 2nd row 3rd position is {num_multi[1, 2]}")
# print(f"Element at the last row last position is {num_multi[len(num_multi)-1, len(num_multi)-1]}")


# nums = n.array([10,20,30,40,50,5,6,35,47,58,65])
#
# condition = nums > 10
# condition1 = nums %2 == 0
#
# filtered_nums = nums[condition]
# even_nums = nums[condition1]
#
# print(nums)
# print(condition)
# print(filtered_nums)
# print(even_nums)
#
#


# numpu slicing [start:stop:step]

nums = n.array([10,20,30,40,50,5,6,35,47,58,65])

print(nums[::]) #print Everything
print(nums)#print everything
print(nums[4:7]) #print 4,5,6 elements
print(nums[::-1]) # print everything but in revers order
print(nums[::2]) # print each alternative element












