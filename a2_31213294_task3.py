"""
NAME Kapish Kuchroo
STUDENT ID 31213294
START DATE: Sunday, 17 May 2020 at 5:34 pm
LAST MODIFIED: Monday, 8 June 2020 at 1:08 pm
"""
"""In Scenario A: when the meeting probability increases it infects more people and count of infected people for less
no of days gets impacted and curves the graph towards affinity.
If we take a large set of meeting probability numbers from which we have to draw a randomly the cure will become more exponential.
In my scenario the affected count is matching the predictions not to the optimal but yes it is matching the predictions.
If I increase the meeting probability the more chances are that pandemic will be spreading at a faster pace."""

import matplotlib.pyplot as plt
from a2_31213294_task2 import *

# import statement to make use of functions/classes from earlier task(s).
# (change the xxxxxxxx to match the actual filename.)


def visual_curve(days, meeting_probability, patient_zero_health):
    days_list = []   #x axis
    contagious_list=run_simulation(days, meeting_probability, patient_zero_health)   #y-axis
    print('List of the contagious people are: ',contagious_list)
    for iteration in range(1,days+1):
        days_list.append(iteration)

    plt.plot(days_list ,contagious_list)      # matplot lib taking x and y axis for printing the graph
    plt.show()


if __name__ == '__main__':
    days_input=int(input('Enter the number of days for the simulation to run    '))
    meeting_probability_input=float(input('Enter the meeting probability in float   '))
    patient_zero_health_input=int(input('Enter the health of patient zero for the simulation    '))
    visual_curve(days_input, meeting_probability_input, patient_zero_health_input)


# do not add code here (outside the main block).
