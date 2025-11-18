import matplotlib.pyplot as p


sub_names = ["Maths", "CS", "Physics", "stats", "English"]
sub_marks = [55,40,60,75,59]
bar_colors = ['tab:green', 'tab:blue', 'tab:red', 'tab:orange']


bars = p.subplots()
chart = p.barh(sub_names, sub_marks,color=bar_colors)
p.title("Subject wise marks")
p.xlabel("SubjectNames")
p.ylabel("SubjectMarks")
p.show()
