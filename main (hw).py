import matplotlib.pyplot as plt
# study school sleep leisure

days=[1,2,3,4,5,6,7]

sleep=[8,8,8,8,8,8,8]
school=[6,6.5,6,5,4,0,0]
leisure=[1,0,2,1,3,3,4]

hrs_sleep=sum(sleep)
hrs_school=sum(school)
hrs_leisure=sum(leisure)

print(max(hrs_leisure,hrs_school,hrs_sleep))



categories=["sleep","school","leisure"]
colors=["blue","green","yellow"]

plt.stackplot(days,sleep,school,leisure,labels=categories,colors=colors)
plt.title("Stack Plot")
plt.legend(loc="upper right")
plt.xlabel("Days")
plt.ylabel("Hours")
plt.show()
