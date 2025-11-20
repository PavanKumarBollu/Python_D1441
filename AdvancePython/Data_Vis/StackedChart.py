# import matplotlib.pyplot as plt
# import numpy as np
#
# sections = ('Section - A', "Section - B", "Section - C", "Section - D")
#
# gender_count = {    "male": [15,25,30,29],    "female": [35,25,20,21], }
# width = .6
# fig, ax = plt.subplots()
# bottom = np.zeros(4)
# for cat,values in gender_count.items():
#     p = ax.bar(sections, values, width, bottom=bottom, label = cat)
#     # p = ax.bar(sections, values, width, color = ["pink", 'lightblue'], bottom=bottom, label = cat)
#     bottom += values
#     ax.bar_label(p, label_type='center')
# ax.set_title("Gender Distribution")
# ax.legend()
# plt.show()



# case 2 :-

import matplotlib.pyplot as plt

sections = ('Section - A', "Section - B", "Section - C", "Section - D")
gender_count = {    "male": [15,25,30,29],    "female": [35,25,20,21], }
width = 0.6
fig, ax = plt.subplots()


male, female = gender_count.items()
print(male[0], male[1], female[0], female[1])

x = ax.bar(sections, male[1], width,  label=male[0], color = "lightgreen")
y = ax.bar(sections, female[1], width, bottom=male[1] ,label=female[0], color = "skyblue")
ax.bar_label(x, padding=3, label_type="center")
ax.bar_label(y, padding=3, label_type="center")

ax.set_title("Gender Distribution")
ax.legend()
plt.show()



# case 3:

# import matplotlib.pyplot as plt
# import numpy as np
#
# categories = ['A', 'B', 'C', 'D']
# data1 = np.array([3, 8, 1, 10])
# data2 = np.array([2, 5, 4, 7])
#
# # Uniform color for the first layer
# plt.bar(categories, data1, color='lightcoral', label='Layer 1')
#
# # Uniform color for the second layer
# plt.bar(categories, data2,color='skyblue', label='Layer 2')
#
# plt.xlabel('Categories')
# plt.ylabel('Values')
# plt.title('Stacked Column Chart with Uniform Layer Colors')
# plt.legend()
# plt.show()