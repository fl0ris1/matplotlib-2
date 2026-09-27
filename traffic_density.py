"""Traffic Density Analysis (Bar + Line)
Real-Life Context: City traffic planning
Task:
Create data for traffic count at different hours of the day.

Plot:

Bar graph → Number of vehicles per hour

Line graph → Trend of traffic growth

Add labels, title, and legend."""

import matplotlib.pyplot as plt
import numpy as np
import random


hours=np.arange(0,24)
vehicles=[]
for i in range(24):
    vehicles.append(random.randint(30,100))

plt.bar(hours,vehicles,color="blue",label="Traffic count")
plt.plot(hours,vehicles,color="red",label="Traffic Growth Trend",marker="o")
plt.legend()
plt.xlabel("Hours")
plt.ylabel("Vehicle Count")
plt.title("Traffic Density Analysis")
plt.show()
