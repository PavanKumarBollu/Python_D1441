# """
# subplots are like photo frames where we can divide the frame into multiple parts and add the pictures accordingly
# here the subplots also exactly same we can add any number of figures into the subplots() from 1toN
#
# when you say the subplots it will create a grid on that grid we can do the partition
# in general we will use the subplots() to do the multiple data set comparison of multiple charts ... etc
# it is kind of similar to power bi reports
#
#
# """
#
# import matplotlib.pyplot as plt
# from pandas.io.sas.sas_constants import subheader_pointer_length_x64
#
# #student data
# student_names = ["PK","AMB","AA","NTR","RC","MB", "RT", "VJK", "SB", "BK","YASH","MGS","SBT","NANI"]
# computer_science = [45,55,66,75,52,36,88,75,74,65,88,69,78,85]
# stats = [52,74,45,36,88,75,55,66,75,65,88,69,78,85]
#
#
# fig, ax = plt.subplots(1,2,figsize=(10,5))
#
# ax[0].bar(student_names, computer_science, color = ["pink",'yellow', 'blue', 'green','purple'])
# ax[1].barh(student_names, stats, color = ["pink",'yellow', 'blue', 'green','purple'])
# plt.show()

# case 2 : -
# vertical subplots()
# import matplotlib.pyplot as plt
#
# student_names = ["PK","AMB","AA","NTR","RC","MB", "RT", "VJK", "SB", "BK","YASH","MGS","SBT","NANI"]
# computer_science = [45,55,66,75,52,36,88,75,74,65,88,69,78,85]
# stats = [52,74,45,36,88,75,55,66,75,65,88,69,78,85]
#
#
# fig, ax = plt.subplots(2,1,figsize=(10,5))
#
# ax[0].bar(student_names, computer_science, color = ["pink",'yellow', 'blue', 'green','purple'])
#
#
# ax[1].barh(student_names, stats, color = ["pink",'yellow', 'blue', 'green','purple'])

# plt.show()

# case 3 : -

import matplotlib.pyplot as plt

student_names = ["PK","AMB","AA","NTR","RC","MB", "RT", "VJK", "SB", "BK","YASH","MGS","SBT","NANI"]
computer_science = [45,55,66,75,52,36,88,75,74,65,88,69,78,85]
stats = [52,74,45,36,88,75,55,66,75,65,88,69,78,85]

fig, ax = plt.subplots(1,2,figsize=(10,5))
chart1 = ax[0].bar(student_names, computer_science, color = ["pink",'yellow', 'blue', 'green','purple'])
ax[0].set_title("CS Marks Comparison")
ax[0].set_xlabel("Student Name")
ax[0].set_ylabel("Computer Science")
ax[0].bar_label(chart1, padding=3)

chart2 = ax[1].barh(student_names, stats, color = ["pink",'yellow', 'blue', 'green','purple'])
ax[1].set_title("Stats Marks Comparison")
ax[1].set_xlabel("Stats Marks")
ax[1].set_ylabel("Student Name")
ax[1].bar_label(chart2, padding=3)

plt.tight_layout() # no overlapping
plt.show()