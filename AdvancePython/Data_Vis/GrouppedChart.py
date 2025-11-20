import matplotlib.pyplot as plt
import numpy as np

studentNames = ('PK',"AA","MB")
sub_wise_marks ={
    "maths":[55,65,45],
    "Cs": [60,45,50],
    "Stats":[80,65,85]
}
label = np.arange(len(studentNames))
width = 0.35
multi = 0
fig, ax = plt.subplots()
for sub_name, sub_marks in sub_wise_marks.items():
    offest = width * multi
    reacts = ax.bar(label+offest, sub_marks,width,label=sub_name)
    ax.bar_label(reacts, padding=2)
    multi += 1

# formatting
ax.set_ylabel("Marks")
ax.set_xlabel("Students")
ax.set_xticks(label+width , studentNames)
ax.legend(loc="upper left")
ax.set_ylim(0,100)

plt.show()
