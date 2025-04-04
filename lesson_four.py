#def greet(name):
#    print("Hello", name)

#greet("David")

#print("Outside function")

#def add_numbers(num1, num2):
#    sum = num1 + num2
#    print("Sum: ", sum)

#add_numbers(5, 4)

#def find_aquare(num):
#    result = num * num
#    return result

#square = find_aquare(3)

#print("Square:", square)

#def future_function():
#    pass

#future_function()

#import math

#square_root = math.sqrt(4)

#print("Square Root of 4 is", square_root)


#power = pow(2, 3)

#print("2 to the power 3 is", power)

#def is_prime(n):
#    if n % 2 == 0:
#        print("Even")
#        return False
#    else:
#        print("Odd")
#        return True

#is_prime(13)

#def add_numbers(a = 7, b = 8):
#    sum = a + b
#    print("Sum:", sum)

#add_numbers(2, 3)
#add_numbers()
#add_numbers(2)

#def display_info(first_name, last_name):
#    print("First Name:", first_name)
#    print("Last Name:", last_name)

#display_info(last_name = "Cartman", first_name = "Eric")

#def find_sum(*numbers):
#    result = 0

#    for num in numbers:
#        result = result + num

#    print("Sum = ", result)

#find_sum(1, 2, 3)

#find_sum(4, 9)

#def full_name(first_name, last_name):
#    return first_name + " " + last_name

#print(full_name("John", "Doe"))

#def add_numbers():
#    sum = 5 + 4


#def greet():
    # local variable
#    message = "Hello"

#    print("Local", message)

#greet()

#GLOBAL

#message = "Hello"

#def greet():
#    print("Local", message)

#greet()
#print("Global", message)

# outside function

# outer():
#    message = "local"



#    def inner():


        # declare nonlocal variable
#        nonlocal message
#        message = "nonlocal"
#        print("inner:", message)

#outer()

#c = 1

#def add():
#    global c
#    c = c + 2
#    print(c)

#add()


#def factorial(x):
#    if x == 1:
#        return 1
#    else:
#        return (x + factorial(x - 1))

#num = 3
#print("The factorial of", num, "is", factorial(num))

#def factorial2(x):
#    if x == 1:
#        return 1
#    else :
#        return (x * factorial2(x - 1))

#print(factorial2(5))

#import example

#example.add(4,5)

#import math

#print("The value of pi is", math.pi)

#import math as m

#print(m.pi)

#from math import pi

#print(pi)

#from math import *

#print("The value of pi is", pi)

#print(dir(example))

#from Game.Level1 import start
#start.select_difficulty(2)

#from Game.Level.start import select_difficulty
#select_difficulty(2)
