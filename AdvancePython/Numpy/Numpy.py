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



import numpy as np

# Minimum Value: -2^63, which is -9,223,372,036,854,775,808
# Maximum Value: 2^63 - 1, which is 9,223,372,036,854,775,807

arr = np.array([1,2,3,4,5], dtype='int64')
print(arr, arr.dtype)

nums = np.array([100,200,300,400,500], dtype='int32')# Minimum value: -2,147,483,648 (which is -2^31) # Maximum value: 2,147,483,647 (which is 2^31 - 1)

print(nums, nums.dtype)

nums16 = np.array([100,145,300,400,32768], dtype='int16') # -32,768 to 32,767.
print(nums16, nums16.dtype)


# 128 + 127 = 255
nums8 = np.array([10,11,12,-128,127], dtype='int8') # -128 to +127 we can store any value but not greater not lesser values
print(nums8, nums8.dtype)





import numpy as np
# uint64, uint32, uint16, uint8


u_num_64 = np.array([1,2,3], dtype='uint64')
print(u_num_64, u_num_64.dtype)

u_num_32 = np.array([1,2,3], dtype='uint32')
print(u_num_32, u_num_32.dtype)

u_num_16 = np.array([1,2,3], dtype='uint16')
print(u_num_16, u_num_16.dtype)

u_num_8 = np.array([1,2,3], dtype='uint8')
print(u_num_8, u_num_8.dtype)




