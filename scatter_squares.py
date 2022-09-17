import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**3 for x in x_values]
#c can be replaced with "color" and a tuple with rgb in a scale from 0 to 1
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.YlGn_r,edgecolors="none",s=10)
#Set chat title and label axes.
plt.title("Square numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#Set size of tick labels
plt.tick_params(axis="both", which="major", labelsize=14)
#Set the range for each axis
#axis(minX,maxX, minY,maxY)
plt.axis([0,1100,0,990000000])

plt.show()