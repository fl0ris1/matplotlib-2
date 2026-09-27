"""Fitness Tracker Dashboard (Scatter + Line)
Real-Life Context: Health & fitness
Task:
Days on x-axis (1–30)

Steps taken on the y-axis

Plot:

Line graph → daily steps

Scatter plot → highlight days above 10,000 steps

Add legend, grid, title."""

import matplotlib.pyplot as plt
import numpy as np
import random

days=np.arange(0,30)
steps=[]
days10k=[]
steps_days10k=[]
for i in range(30):
    steps.append(random.randint(5000,15000))

plt.plot(days,steps,label="Steps per Day",color="blue")

for i in range(len(steps)):
    if steps[i]>10000:
        steps_days10k.append(days[i])
        days10k.append(steps[i])

plt.scatter(steps_days10k,days10k,label="Above 10k steps",color="red")
plt.xlabel("Days")
plt.ylabel("Steps")
plt.legend()
plt.title("Fitness Tracker Dashboard")
plt.show()