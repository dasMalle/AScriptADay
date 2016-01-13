import time

#Greets the guest and asks for his name
print("Hello you, what is your name?")
guestName = input()
print("Very nice to meet you, " + guestName)
print("'Press ENTER to start the stopwatch. Afterwards press ENTER to stop it'")

#stop time
input()
print("started")
startTime = time.time()
input()
stoppedTime = time.time() -startTime
print("time: " + str(round(stoppedTime, 2)) +"seconds")


