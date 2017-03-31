#Seconds to hours/min/seconds

secinput=input("Input any number of seconds between 0 and 86,400")
sec=float(secinput)

hours=sec//3600
secremain=sec%3600

minutes=secremain//60
secremain=secremain%60

seconds=secremain

print(hours, "hours", minutes, "minutes, and", seconds, "seconds.")
