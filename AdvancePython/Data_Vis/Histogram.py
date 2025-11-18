"""
histogram is a visual representation which is used for comparing the frequency of the data distribution

for example : whe we have student marks with us like 20 students and we want to understand the range of students by
dividing them in ranges like 30-40, 40-50, 60-70, ...etc to do this we can take the help of histogram chart
for visual representation

"""

arr_ranges = [0,10,20,30,40,50,60,70,80,90,100]
std_marks = [35,25,14,6,52,14,5,44,88,75,45,65,21,54,23,23,63,69,65,68,
             45,68,78,98,89,88,65,62,45,54,55,56,12,32,26,35,30,34,36,65,
             65,85,74,58,47,58,46,45,96,69,70,87,78]

import matplotlib.pyplot as plt

plt.hist(std_marks, bins=arr_ranges, edgecolor='black',color='lightgreen')
plt.xlabel("Range")
plt.ylabel("Frequency")
plt.show()