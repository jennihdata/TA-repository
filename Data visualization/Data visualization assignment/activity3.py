import csv
import pygal

from matplotlib import pyplot as plt
from datetime import datetime


filename = 'activity.csv'
with open (filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
# #3-1
#     # total = 0
#     # for row in reader:
#     #     if row[0] == 'NA':
#     #         total += 1
#     # print(total)
#
# #3-2
    list1 = []
    for row in reader:
        if row[0] == 'NA':
            row[0] = 1
            list1.append(row)
    print(list1)
#
#     hist = pygal.Bar()
#     hist.title = "Total number of steps taken each day"
#     hist.x_labels = rows
#     hist.x_title = "Number Of Days "
#     hist.y_title = "Number of Steps "
#     hist.add("rows", row)
#     hist.render_to_file("histogram2.svg")
#
