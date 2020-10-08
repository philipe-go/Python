x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

"""
Function VS Methods
A function is a block of code to carry out a specific task, will contain its own scope and is called by name. 
A method is somewhat similar to a function, except it is associated with object/classes
"""
#overloaded function has to initialize the variables in the declartion
#however, it can be called passing an argument value or none
def isEven(x = 0, m=0):
    if x%2 == 0:
        return True
    return False
    pass

def isPrime(n):
    flag = True
    for x in range(2,n):
        if n%x == 0:
            flag = False
            break
    return flag;

#recursive function
def factorial(n):
    if (n==0): return 1
    else: return n * factorial(n-1)

##calling the function
print(f"The number {x} is even? {isEven(x)}")
print(f"overloaded function no arg {isEven()}")
print(f"overloaded function two args {isEven(x,y)}")
print(f"{x} is a prime number? {isPrime(x)}")
print(f"factorial of {y} = {factorial(y)}")


##calling methods with the class name
import math

print(math.sin(x))
print(math.log10(int(y)))
print(math.sqrt(int(x+y)))

##calling methods within the class ALIAS name
import cmath as cm

print(cm.sqrt(int(x)+4j))


##calling methods without calling the class name
from math import sin, log10, sqrt

print(sin(int(x)))
print(log10(int(y)))
print(sqrt(int(x+y)))
