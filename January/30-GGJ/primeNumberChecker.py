# sorry for the short simple script and the late upload, but I scripted all day in c# cause GGJ is going on :)
import math

#Boom primeNumbers in super short
def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

print("check if this number is a prime number: ")
num = input()
print(is_prime(int(num)))