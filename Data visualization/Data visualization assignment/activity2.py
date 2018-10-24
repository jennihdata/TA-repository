import csv
import pygal

from matplotlib import pyplot as plt
from datetime import datetime


filename = 'activity.csv'
with open (filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dict = {}
    for row in reader:
        if row[0] == 'NA':
            continue

        else:
            dict.setdefault(row[2], [])
            dict[row[2]].append(int(row[0]))

    average, intervals = [], []

    for values in dict.values():
        sum_values = sum(values)
        avg = int(sum_values)//len(values)
        average.append(avg)
    # print(len(list1))

    for keys in dict.keys():
        intervals.append(int(keys))
    # print(intervals)

    plt.plot(intervals, average)
    plt.title("Daily Activity Steps")
    plt.xlabel("Intervals")
    plt.ylabel("Average Steps")
    plt.show()

#max number of steps interval

    max_steps = max(average)
    max_steps_index = average.index(max_steps)
    max_intervals = intervals[max_steps_index]
    print(max_intervals)