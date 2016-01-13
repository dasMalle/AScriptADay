import datetime as dt
import os

print("hey when would you like to shutdown your computer? (hh:mm)")
st = input()
h, m = st.split(':')
now = dt.datetime.now()
later = dt.datetime(now.year, now.month, now.day, int(h), int(m))

seconds = (later - now).total_seconds()
if seconds > 0:
    print("will be shutdown in " + str(seconds) + "seconds")
    os.system("shutdown -s -t " + str(int(seconds)))
else:
    print("That's not happening today")