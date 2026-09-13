import matplotlib.pyplot as plt
import numpy as np

#histogram frequency chart
ages=[30,35,40,45,50,55,60,65,70,75,80]
bins=[20,30,40,50,60]
plt.hist(ages,bins,edgecolor='black',color='blue')
plt.title("Histogram Frequency Chart")
plt.xlabel("Ages")
plt.ylabel("Frequency")
plt.show()

#scatter plot
x=[5,3,7,4,2,6]
y=[3,5,2,1,6,7]
plt.scatter(x,y,color='blue')
plt.title("Scatter Plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()

#pie chart
categories=["sleep","school","work","other"]
percentages=[33,30,25,12]
colors=["lightblue","cyan","red","pink"]
plt.pie(percentages,labels=categories,colors=colors,startangle=90,autopct="%1.1f%%")
plt.title("Pie Chart")
plt.axis("equal")
plt.show()


#stack plot
days=[1,2,3,4,5,6,7]
sleep=[8,8,8,8,8,8,8]
school=[7,5,6,6,3,0,0]
work=[0,3,3,0,0,5,3]
categories=["sleep","school","work"]
colors=["lightblue","cyan","red"]

plt.stackplot(days,sleep,school,work,labels=categories,colors=colors)
plt.title("Stack Plot")
plt.legend(loc="upper left")
plt.xlabel("Days")
plt.ylabel("Hours")
plt.show()