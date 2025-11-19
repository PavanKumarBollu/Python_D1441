import matplotlib.pyplot as plt


#data 1
student_cs = ["PK","AMB","AA","NTR","RC","MB", "RT","NANI"]
computer_science = [75,74,65,88,69,78,78,50]

#data 2
student_stats = ["VJK", "SB", "BK","YASH","MGS","SBT","NANI"]
stats = [52,74,45,36,88,75,55]

# data 3 pie
brands = ["Nike", "Livis", "ZARA", "H&M", "BMW", "USPolo"]
total_sales = [1000,1200,600,700,1300,800]

#data 4 histogram
arr_ranges = [0,10,20,30,40,50,60,70,80,90,100]
std_marks = [35,25,14,6,52,14,5,44,88,75,45,65,21,54,23,23,63,69,65,68,
             45,68,78,98,89,88,65,62,45,54,55,56,12,32,26,35,30,34,36,65,
             65,85,74,58,47,58,46,45,96,69,70,87,78]

#data 5 plot
arr_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr_2 = [11, 12, 13, 5, 15, 1, 7, 18, 9, 20]


fix, ax = plt.subplots(2, 3,figsize=(12,7))

chart1= ax[0,0].bar(student_cs,computer_science,color = ["pink",'yellow', 'blue', 'green','purple'], zorder = 5)
ax[0,0].set_title("CS_Marks_Comparison")
ax[0,0].set_xlabel("Computer Science")
ax[0,0].set_ylabel("Marks")
ax[0,0].bar_label(chart1, padding=3)
ax[0,0].grid(True, color='gray', zorder=-1)

chart2 = ax[0,1].barh(student_stats, stats, color = ["pink",'yellow', 'blue', 'green','purple'], zorder = 5)
ax[0,1].set_title("Stats_Marks_Comparison")
ax[0,1].set_xlabel("Statistics")
ax[0,1].set_ylabel("Marks")
ax[0,1].bar_label(chart2, padding=3)
ax[0,1].grid(True, color='gray', zorder=-1)

ax[0,2].pie(total_sales, labels=brands, colors=["pink",'yellow', 'blue'], autopct='%1.2f%%')
ax[0,2].set_title("Sum of Sales")
ax[0,2].grid(True, color='gray', zorder=-1)

ax[1,0].hist(std_marks, bins=arr_ranges, edgecolor='black',color='lightgreen', zorder = 5)
ax[1,0].set_title("Marks Frequency Distribution")
ax[1,0].set_xlabel("Range")
ax[1,0].set_ylabel("Frequency")
ax[1,0].grid(True, color='gray', zorder=-1)

ax[1,1].plot(arr_1, arr_2 , zorder = 5)
ax[1,1].set_title("LinePlot")
ax[1,1].grid(True, color='gray', zorder=-1)



ax[1,2].set_title("Empty Slot for Feature Purpose")


plt.grid(True)

plt.tight_layout() # no overlapping
plt.show()