import pygal
from random import randint

class Die():
    """A class representing a single die."""
    def __init__(self, num_sides=6):
        """Define the number of sides a dice has, assume 6"""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and the number of sides"""
        return randint(1,self.num_sides)

#Create two dice

die_1 = Die(10)
die_2 = Die(8)

#Make some rolls and store them in a list
results = []
for roll_num in range(100000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#Analize the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)


#Visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling a D{} and a D{} - {} times".format(die_1.num_sides, die_2.num_sides,len(results))

#Create a list containing all the possible labels
num_labels =[]
for i in range(2,die_1.num_sides+die_2.num_sides+1):
    num_labels.append(str(i))



hist.x_labels = num_labels
hist.x_title = "Result"
hist.y_title = "Frequency of result"

hist.add("d{}+d{}".format(die_1.num_sides,die_2.num_sides), frequencies)
hist.render_to_file("die_visual.svg")
