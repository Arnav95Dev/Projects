import time

hours = int(input("Set the hours: "))
minute = int(input("Set the minutes: "))
seconds = int(input("Set the seconds: "))

total_time = (hours*3600) + (minute*60) + seconds

while total_time > 0:
    time.sleep(total_time)
else:
    print("Wake up!!")