"""Homework—Plot the bar graphs of the total number of men and women in the
Titanic, the average fare of men and women, and the pie chart for the number of |
people of different classes present. The Titanic dataset should be interpreted to"""

import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv("cw/titanic.csv")
male=data[(data["Sex"]=="male")]
female=data[(data["Sex"]=="female")]

plt.bar(["Male","Female"],[len(male),len(female)])
plt.title("Males And Females on the Titanic")
plt.ylabel("Passenger Count")
plt.show()

"??????????????????????????????????????"

class1=data[(data["Pclass"]==1)]
class2=data[(data["Pclass"]==2)]
class3=data[(data["Pclass"]==3)]
plt.pie([len(class1),len(class2),len(class3)],labels=["Class 1","Class 2", "Class 3"],colors=["lightblue","cyan","red","pink"],startangle=90,autopct="%1.1f%%")
plt.title("Pie Chart of passengers in classes")
plt.axis("equal")
plt.show()

