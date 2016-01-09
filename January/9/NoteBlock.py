import datetime
file = open('Noteblock.txt', 'a')

print("Just enter your notes here and they will be saved with the current date and time")
note = input()

file.write("\n"+note + " " + datetime.datetime.now().strftime("%B %d, %Y"))

file.close()
