

""" print the tables from 2 to 20 """
from turtledemo.penrose import start

# num = 2
# count = 1
#
# while num <= 20:
#     while count <= 10: # 11 <= 10
#         print(f"{num } x {count} = {num * count}")
#         count += 1 # count will become 10 or more than ten
#     num += 1 # 2 -> 3 --> 4
#     count = 1


num = 1
count = 1

while count <= 10:
    while num <= 20:
        print(f"{num } x {count} = {num * count}", end= "| ")
        num += 1
    count += 1
    print()
    num = 1



