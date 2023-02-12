import datetime

current_time = datetime.datetime.now()

print(current_time)

now  = current_time.strftime("%H : %M : %S")
hour  = current_time.strftime("%H")


print(now)
print(hour)

date = current_time.strftime("%d/ %m / %y")

print(date)