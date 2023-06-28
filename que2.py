#2)	Write a python program to check whether the given number is prime or not.

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(num/2)+1):
        if n % i == 0:
            return False
    
    return True

num = 18
if is_prime(num):
    print(" it is a prime number.")
else:
    print("it is not a prime number.")