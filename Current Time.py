import time

cur_time = time.asctime().split(" ")
print(cur_time)
clock = cur_time[-2].split(":")
if int(clock[2]) == 1 or int(clock[2] == 0):
    status_2 = 'second'
else:
    status_2 = 'seconds'
if int(clock[0]) >= 12:
    status = "pm"
else:
    status = "am"

print(f'Now is {cur_time[1]} {cur_time[-3]} {cur_time[-1]} {clock[0]}:{clock[1]}{status} {clock[2]}{status_2}')
