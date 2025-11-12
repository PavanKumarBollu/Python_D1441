# pip install numpy

# import numpy as np
#
# print(np.__version__)

"""
numpy provides veriaty of datatypes to work with large data


numpy dataType
--------------
int64, int32, int16, int8
uint64, uint32, uint16, uint8
float64,float32,float16 
bool
object
string
datetime64
timedelta64
"""
# int64, int32, int16, int8



# import numpy as np
# 
# # Minimum Value: -2^63, which is -9,223,372,036,854,775,808
# # Maximum Value: 2^63 - 1, which is 9,223,372,036,854,775,807
# 
# arr = np.array([1,2,3,4,5], dtype='int64')
# print(arr, arr.dtype)
# 
# nums = np.array([100,200,300,400,500], dtype='int32')# Minimum value: -2,147,483,648 (which is -2^31) # Maximum value: 2,147,483,647 (which is 2^31 - 1)
# 
# print(nums, nums.dtype)
# 
# nums16 = np.array([100,145,300,400,32768], dtype='int16') # -32,768 to 32,767.
# print(nums16, nums16.dtype)
# 
# 
# # 128 + 127 = 255
# nums8 = np.array([10,11,12,-128,127], dtype='int8') # -128 to +127 we can store any value but not greater not lesser values
# print(nums8, nums8.dtype)



#
#
# import numpy as np
# # uint64, uint32, uint16, uint8
#
#
# u_num_64 = np.array([1,2,3], dtype='uint64')
# print(u_num_64, u_num_64.dtype)
#
# u_num_32 = np.array([1,2,3], dtype='uint32')
# print(u_num_32, u_num_32.dtype)
#
# u_num_16 = np.array([1,2,3], dtype='uint16')
# print(u_num_16, u_num_16.dtype)
#
# u_num_8 = np.array([1,2,3], dtype='uint8')
# print(u_num_8, u_num_8.dtype)

#
# # float64,float32,float16
# import numpy as np
#
# nums_64 = np.array([1.05,102.8,10.8,14.6,25.0], dtype="float64")
# print(nums_64 , nums_64.dtype)
#
# nums_32 = np.array([1.05,102.8,10.8,14.6,25.0], dtype="float32")
# print(nums_32 , nums_32.dtype)
#
# nums_16 = np.array([1.05,102.8,10.8,14.6,25.0], dtype="float16")
# print(nums_16 , nums_16.dtype)
#
# # bool
# values = np.array([True, False, True, True, False], dtype="bool")
# print(values , values.dtype)
#
# # object
# array_object = np.array(["PL",12, 20.5, True, '2024-06-15'])
# print(array_object , array_object.dtype)
#
# # string
# array_string = np.array(["Pavan","MSC", "HYD", 'Madhpaur'])
#
#
# # datetime64
# array_datetime = np.array(['2024-06-06', '2025-11-12'], dtype="datetime64")
# print(array_datetime , array_datetime.dtype)
#

import numpy as np


nums = [1,2,3,4,5,6,1,2,3,4,5,65,15,2,1,4,2]
print(nums, type(nums))
nums_array = np.array(nums)
print(nums_array, nums_array.dtype) #default datatupe for this is int64

# #generate the values from 10 to 20
# nums = np.arange(start=10,stop=21)
# print(nums, nums.dtype)
#
# #generate the array with default values as zero or one
# nums_zeros = np.zeros((2,3), dtype=int)
# print(nums_zeros, nums_zeros.dtype)

# #ones
# nums_ones = np.ones((2,3), dtype=int)
# print(nums_ones, nums_ones.dtype)

# #generate random array
# nums_random = np.random.rand(3,4)
# print(nums_random)

#generate random array with specific range inputed values
# nums_random1 = np.random.randint(low=10,high=20,size=50)
# print(nums_random1)


#generate an array with user mentioned default value


default_value = int(input("Enter the default value : "))

nums_user_default = np.full((2,3),default_value)
print(nums_user_default, nums_user_default.dtype)

nums_user_default1 = np.random.randint(low=default_value, high=default_value+1, size=10)
print(nums_user_default1, nums_user_default1.dtype)










