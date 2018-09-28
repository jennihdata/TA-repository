initial_velocity = 0
time =int(input("Time: "))
acceleration =int(input("Acceleration: "))
distance =int(input("Distance: " ))
speed_limit = 60
distancelist = []
timeList = [i for i in range (time+1)]

def speed(initial_velocity, acceleration, time):
    return initial_velocity + acceleration*time

def dist(initial_velocity,acceleration,time):
    return initial_velocity*time + ((0.5) * acceleration * time**2)

print("The * indicates every 10m")

duration = 0
s= 0

while duration <= time:
    #print (str(initial_velocity) + " " + str(duration) + " " + str(acceleration))
    s = int(dist(initial_velocity, acceleration, duration))

    i = ""
    distancelist.append(s)
    while s >= 10:
        i += "* "
        s = s - 10

    print("Duration: " + str(duration) +" / Distance: " + str(i))
    duration = duration + 1

dist(initial_velocity,acceleration,time)
if speed(initial_velocity,acceleration,time) > speed_limit:
    print("The person went over the speed limit. " + "(Max speed was " + str(speed(initial_velocity,acceleration,time)) + " m/s)")
else:
    print("The person did not go over the speed limit. " + "(Max speed was "+ str(speed(initial_velocity,acceleration,time)) + " m/s)")

if distance > s:
    print("The person reached the destination. (Reached " + str(dist(initial_velocity,acceleration,time)) + " m)")
else:
    print("The person did not reach the destination. (Reached " + str(dist(initial_velocity,acceleration,time)) + " m)")

import matplotlib.pyplot as plt
plt.plot(timeList,distancelist)
plt.xlabel("Time(s)")
plt.ylabel("Distance(m)")
plt.show()

