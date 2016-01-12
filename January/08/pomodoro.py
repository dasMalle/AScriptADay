import schedule
import time
import winsound


def job():
    winsound.PlaySound(sound, winsound.SND_FILENAME)

print("Welcome you! This is a pomodoro, once started it will remind you to move once a while by playing a sound."
      "\n Please enter the path to the sound you want to play")
sound = input()
print("Now please enter the interval (min) in which you would like to be reminded")
interval = input()
schedule.every(float(interval)).minutes.do(job)
print("ok")
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)