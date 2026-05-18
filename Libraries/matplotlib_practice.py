# import matplotlib
# print(matplotlib.__version__)

# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd

# x = np.array([2023, 2024, 2025, 2026])
# y = np.array([15, 25, 30, 20])

# plt.plot(y)
# plt.plot(x, y)
# plt.show()

# Plot Customization

# x = np.array([2023, 2024, 2025, 2026])
# y1 = np.array([15, 25, 30, 20])
# y2 = np.array([17, 23, 38, 5])
# y3 = np.array([13, 15, 20, 30])

# line_style = dict(marker = ".",
#                   markersize = 30,  # ms = 30 also works
#                   markerfacecolor = "#1cd3fc",  # mfc = "red" also works
#                   markeredgecolor = "#1cd3fc",  # mec = "red" also works
#                   linestyle = "solid",
#                   linewidth = 4)

# plt.plot(x, y1, marker = ".",
#                      markersize = 30,  # ms = 30 also works
#                      markerfacecolor = "#1cd3fc",  # mfc = "red" also works
#                      markeredgecolor = "#1cd3fc",  # mec = "red" also works
#                      linestyle = "solid",
#                      linewidth = 4,
#                      color = "#1c5bfc")

# plt.plot(x, y1, color = "#1c5bfc", **line_style) # ** to unpack the dictionary
# plt.plot(x, y2, color = "#1cfc45", **line_style)
# plt.plot(x, y3, color = "#fc1c1c", **line_style)

# plt.show()

# Labels

# x = np.array([2023, 2024, 2025, 2026])
# y1 = np.array([15, 25, 30, 20])
# y2 = np.array([17, 23, 38, 5])
# y3 = np.array([13, 15, 20, 30])

# plt.title("Class Size", fontsize = 25,
#                              family = "Times New Roman",
#                              fontweight = "bold",
#                              color = "#2d4cfc")

# plt.xlabel("Year", fontsize = 20,
#                          family = "Arial",
#                          fontweight = "bold",
#                          color = "#2dbefc")

# plt.ylabel("Students", fontsize = 20,
#                          family = "Arial",
#                          fontweight = "bold",
#                          color = "#2dbefc")

# plt.tick_params(axis = "both",
#                 colors = "black")

# plt.plot(x, y1)
# plt.plot(x, y2)
# plt.plot(x, y3)

# plt.xticks(x)

# plt.show()

# Grid Lines

# grid() = Helps make plots easier to read by adding reference lines.

# x = [1, 2, 3, 4, 5]
# y = [5, 10, 15, 20, 25]

# plt.plot(x, y)
# plt.grid()
# plt.grid(axis = "y",
#          linewidth = 2,
#          color = "lightgray",
#          linestyle = "--",)

# plt.show()

# Bar Charts

# Bar chart = compare categories of data by representing each category with a bar

# categories = ["Grains", "Fruit", "Vegetables", "Protein", "Dairy", "Sweets"]
# values = np.array([4, 3, 2, 5, 3, 1])

# plt.bar(categories, values, color = "skyblue", alpha = 1)
# plt.barh(categories, values, color = "skyblue", alpha = 1) # for horizontal bar chart

# plt.title("Daily Consumption",fontsize = 25,
#                                    family = "Times New Roman",
#                                    fontweight = "bold")
# plt.xlabel("Food", fontsize = 20,
#                          family = "Arial",
#                          fontweight = "bold")
#
# plt.ylabel("Quantity", fontsize = 20,
#                              family = "Arial",
#                              fontweight = "bold")

# plt.show()

# Pie Charts

# Bar chart = Circular chart divided into slices to show percentages of the total.
#             Good for visualizing distribution among categories.

# categories = ["Freshmen", "Sophomores", "Juniors", "Seniors"]
# values = np.array([300, 250, 275, 225])
# colors = ["red", "yellow", "blue", "green"]

# plt.pie(values, labels = categories,
#                 autopct = "%1.1f%%", # %% to show % as single % is for format specifier
#                 colors = colors,
#                 explode = [0, 0 , 0, 0.2],
#                 shadow = True,
#                 startangle = 90)

# plt.title("Pokemon College", fontsize = 25,
#                                   family = "Times New Roman",
#                                   fontweight = "bold")

# plt.show()

# Scatter Graphs

# scatter graph = Shows the relationship between two variables
#                 Helps to identify a correlation (+,-, None)
#                 Example: Study hours vs. Test scores

# x1 = np.array([0, 1, 1, 2, 3, 4, 5, 6, 7, 7, 8]) # Hours Studied
# y1 = np.array([55, 60, 65, 62, 68, 70, 75, 78, 82, 85, 87]) # Grades

# x2 = np.array([0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 8]) # Hours Studied
# y2 = np.array([50, 58, 65, 70, 72, 78, 83, 88, 92, 95, 97]) # Grades

# plt.scatter(x1, y1, color = "skyblue",
#                     s = 200,
#                     label = "Class A")

# plt.scatter(x2, y2, color = "red",
#                     alpha = 0.7,
#                     s = 200,
#                     label = "Class B")

# plt.title("Test Scores")
# plt.xlabel('Hours Studied')
# plt.ylabel('Grade')
# plt.legend()
# plt.show()

# Histograms

# Histogram = A visual representation of the distribution of quantitative data.
#             They group values into bins (intervals)
#             and counts how many fall in each range.

# scores = np.random.normal(loc = 80, scale = 10, size = 100)
# scores = np.clip(scores, 0, 100) # a_min=0, a_max=100, makes min and max scores b/w 0 and 100

# plt.hist(scores, bins = 10, # No. of towers
#                  color = 'skyblue',
#                  edgecolor = 'black')

# plt.title("Exam Scores")
# plt.xlabel("Score")
# plt.ylabel("# of Students")
# plt.show()

# Subplots

# Figure = The entire canvas
# Ax = A single plot (subplot) technically a numpy array

# x = np.array([1, 2, 3, 4, 5])
# figure, axes = plt.subplots(2,2)
# axes[0,0].plot(x, x*2, color = "red")
# axes[0,0].set_title("x*2")
# axes[0,1].plot(x, x**2, color = "blue")
# axes[0,1].set_title("x**2")
# axes[1,0].plot(x, x**3, color = "green")
# axes[1,0].set_title("x**3")
# axes[1,1].bar(x, x**4, color = "yellow")
# axes[1,1].set_title("x**4")

# plt.tight_layout()
# plt.show()

# Pandas + Matplotlib

# df = pd.read_csv("data.csv")
# type_count = df["Type1"].value_counts(ascending=True)

# plt.barh(type_count.index, type_count.values, color = "#03ddfc",
#                                               edgecolor = "black")
# plt.title("# of Pokemon by Primary Type")
# plt.xlabel("Count")
# plt.ylabel("Type")
# plt.tight_layout()
# plt.show()