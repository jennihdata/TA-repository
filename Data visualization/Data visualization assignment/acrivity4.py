import csv
import matplotlib.pyplot as plt

def Reset():
    weekday_total = 0
    weekend_total = 0
    weekday_count = 0
    weekend_count = 0

filename = "activity.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    interval = []
    x = 0
    weekday_total = 0
    weekend_total = 0
    weekday_count = 0
    weekend_count = 0
    weekendstepavg = []
    weekdaystepavg = []
    day = 0

    while x < 2360:
        interval.append(x)
        x += 5

    for i in range(0, len(interval)):
        f.seek(0)
        next(f)
        for row in reader:
            if int(row[2]) == int(interval[i]):
                if day % 7 < 5:
                    try:
                        stepNo = int(row[0])
                    except ValueError:
                        day += 1
                        continue
                    else:
                        weekday_total += stepNo
                        weekday_count += 1
                        day += 1
                else:
                    try:
                        stepNo = int(row[0])
                    except ValueError:
                        day += 1
                        continue
                    else:
                        weekend_total += stepNo
                        weekend_count += 1
                        day += 1
        try:
            weekendstepavg.append(weekend_total / weekend_count)
        except ZeroDivisionError:
            weekendstepavg.append(0)
        try:
            weekdaystepavg.append(weekday_total / weekday_count)
        except ZeroDivisionError:
            weekdaystepavg.append(0)
        day = 0
        weekday_total = 0
        weekend_total = 0
        weekday_count = 0
        weekend_count = 0

plt.scatter(interval, weekendstepavg, cmap=plt.cm.Reds, edgecolors='black', s=35)
plt.scatter(interval, weekdaystepavg, cmap=plt.cm.Blues, edgecolors='green', s=35)
plt.legend(["weekend step avg", "weekday step avg"])
plt.xlabel("interval", fontsize=10)
plt.ylabel("Average steps", fontsize=10)
plt.axis([0, 2400, 0, 300])
plt.show()
