"""Monthly Household Expense Breakdown (Pie Chart)
Real-Life Context: Personal finance
Task:
Create monthly expenses:

Rent

Food

Transport

Entertainment

Savings

Plot a pie chart with:

Custom colors

Shadow

Start angle

Show percentage contribution."""

import matplotlib.pyplot as plt
expenses=[1000,200,50,100,500]
categories=["Rent","Food","Transport","Entertainment","Savings"]
colors=["red","green","blue","yellow","purple"]

plt.pie(expenses,labels=categories,colors=colors,autopct="%1.1f%%",startangle=90)
plt.title("Monthly Household Expense Breakdown")
plt.axis("equal")
plt.show()