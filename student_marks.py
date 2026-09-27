'''Student Marks Distribution (Histogram)
Real-Life Context: School performance analysis
Task:
Generate marks of 50 students (0–100).

Plot a histogram with appropriate bins:

0–30

31–50

51–70

71–90

91–100

Label grade ranges clearly.

Bonus Challenge:
Print the number of students scoring above 75.'''

import matplotlib.pyplot as plt
import numpy as np
import random

bins=[0,30,50,70,90,100]
plus75=0
student_score=[]
for i in range(50):
    score=random.randint(0,100)
    student_score.append(score)
    if score>75:
        plus75+=1

print(plus75)

plt.hist(student_score,bins,edgecolor='white',color='blue')
plt.title("Marks of 50 Students")
plt.xlabel("Bins")
plt.ylabel("Marks")
plt.show()

