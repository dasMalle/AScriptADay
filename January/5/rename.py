import os

print("Hey mate would you like to rename some files? [y/n]")
ans = input()
if ans is "y":
    print("Please enter the path to the directory. Keep in mind I will rename all the files in the directory! "+
          "They will be numbered starting at 1")
    ans = input()
    i = 1
    if os.path.isdir(ans):
        for fn in os.listdir(ans):
            # os.rename(str(ans +"/" +fn), str(i))
            filename, ext = fn.split(".")
            os.rename(os.path.join(ans, fn), os.path.join(ans, str(i)+"."+ext))
            i += 1
        print("Cool, done")
    else:
        print("invalid path")
else:
    print("Alright, take care")
