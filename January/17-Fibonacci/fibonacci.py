print("please enter how many fibonacci numbers you want")
threshold = int(input())
a,b = 1,1
fib = "0, "
for i in range(threshold-1):
    fib+= str(a+b)+", "
    a,b = b, a+b

print(fib)