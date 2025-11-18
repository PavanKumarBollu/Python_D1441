"""
Pie chart is best suited when we were comparing the values below 7 bcz when the values are more than 7 the comparision
of the values will become difficult

"""

brands = ["Nike", "Livis", "ZARA", "H&M", "BMW", "USPolo"]
total_sales = [1000,1200,600,700,1300,800]

import matplotlib.pyplot as plt
pie_colrs = ['red', 'green', 'blue', 'orange', 'purple', 'pink']

plt.pie(total_sales, labels=brands, colors=pie_colrs, autopct='%1.2f%%')
plt.title("Sum of Sales")
plt.legend(brands, loc="center left", bbox_to_anchor=(-0.25, 0.5))
plt.show()

