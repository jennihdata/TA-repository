import csv
import pygal

from matplotlib import pyplot as plt
from datetime import datetime


filename = 'activity.csv'
with open (filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)


    dates, steps, intervals = [], [],[]
    steps_total = 0
    current_date = 0
    for row in reader:
        current_dates = datetime.strptime(row[1], "%Y-%m-%d")
        if current_dates == current_date:
            if row[0] != "NA":
                step = int(row[0])
                steps_total +=  step
        else:
            current_date = datetime.strptime(row[1], "%Y-%m-%d")
            steps.append(steps_total)
            steps_total = 0
            if row[0] != "NA":
                step = int(row[0])
                steps_total += step

    steps.append(steps_total)
    interval = int(row[2])
    intervals.append(interval)

del steps[0]
# print(steps)

#histogram

hist = pygal.Bar()
hist.title = "Total number of steps taken each day"
hist.x_labels = steps
hist.x_title = "Number Of Days "
hist.y_title = "Number of Steps "
hist.add("steps", steps)
hist.render_to_file("histogram.svg")

#mean

sum_steps = sum(steps)
mean = sum_steps // len(steps)
print("Mean = ",mean)

#median

sorted_list = sorted(steps)
num_median = (len(sorted_list))/2
median = sorted_list[int(num_median)]
print ("Median = ",median)



