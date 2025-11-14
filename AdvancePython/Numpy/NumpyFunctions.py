# Copy() view()
import numpy as np
from numpy.ma.core import indices

#Array view is nothing but creating a one more different view in the memory and assigning some variable for reference purpose
#
# nums_original = np.array([10,20,30,40,50,23,24,25])
# print(nums_original)
#
# nums_view = nums_original.view()
# print(nums_view)
#
# nums_original[2] = 31
# print(nums_original)
#
# print(nums_view)

#arrays copy() method will copies the exact array and when you modify the original array it will not effect the copied array

# nums_original = np.array([10,20,30,40,50,23,24,25])
# print(nums_original)
#
# nums_copy = nums_original.copy()
# print(nums_copy)
# nums_original[2] = 31
# print(nums_original)
# nums_copy[2] = 123
#
# print(nums_copy)


# mean()
# nums= np.array([10,20,30,40,50,23,2,24,25])
# avg = np.average(nums)
# avg_value = nums.mean()
# print(avg_value)
# print(avg)
#
# print(nums.min())
# print(nums.max())
#
# # argmax() argmin()
# print(nums.argmin()) #6
# print(nums.argmax()) #4



# split()
# nums= np.array([10,20,30,40,50,23,10,12,13,14,15,17])
#
# # split(arr, indices 0r sections)
# # arr --> original array which we want to split into part
# # indices or sections -- > how many number of part we want to divide the main array basically this will be an integer
#
# print(nums)
#
# sub_nums = np.split(nums, 3)
# for subs in sub_nums:
#     print(subs, end=" ")
# # print(sub_nums)
# print()
#
# # sub_nums_indecies = np.split(nums, [2,4,6,8,10])
# sub_nums_indecies = np.split(nums, [3,6,9])
# # sub_nums_indecies = np.split(nums, [4,8,])
# for sub in sub_nums_indecies:
#     print(sub)



# sort()
# nums = np.array([5,4,6,7,3,8,2,8,1,22,36,54,12,10,78])
# print(nums)
#
# nums_sorted = np.sort(nums)  # default sorting is quick sort
# print(f"sorted array : {nums_sorted}")
#
# nums_desc = np.sort(nums)[::-1]  # default sorting is quick sort
# print(f"sorted array : {nums_desc}")
#
# print(f"original array after sorting : {nums}")






# inplace sorting
nums_asen1 = np.array([5,4,6,7,3,8,2,8,1,22,36,54,12,10,78])
nums_desc1 = np.array([5,4,6,7,3,8,2,8,1,22,36,54,12,10,78])

print(f"nums_asen1: {nums_asen1}")
nums_asen1.sort() # default sorting is quick sort
print(f"nums_asen1 after sorting: {nums_asen1}")

print(f"nums_desc: {nums_desc1}")

nums_desc1[::-1].sort()  # default sorting is quick sort

print(f"nums_desc after sorting: {nums_desc1}")

nums_asen1 = np.array([5,4,6,7,3,8,2,8,1,22,36,54,12,10,78])



print(f"nums_asen1: {nums_asen1}")
nums_asen1.sort( kind="mergesort") # default sorting is quick sort
print(f"nums_asen1 after sorting: {nums_asen1}")




