# import matplotlib as plt
# print(plt.__version__)



#
# import matplotlib.pyplot as plt
#
# arr_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# arr_2 = [11, 12, 13, 5, 15, 1, 7, 18, 9, 20]
#
#
# #create the line plot using arr_1 , arr_2
# plt.plot(arr_1, arr_2)
# plt.title("line chart")
# plt.show()


# create the bar chart for the following student data

import matplotlib.pyplot as p


sub_names = ["Maths", "CS", "Physics", "stats", "English"]
sub_marks = [55,40,60,75,59]

bars = p.subplots()
chart = p.bar(sub_names, sub_marks)
p.title("Subject wise marks")
p.xlabel("SubjectNames")
p.ylabel("SubjectMarks")
p.show()













