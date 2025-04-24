
#my_list = [4, 7, 0]

#iterator = iter(my_list)

#print(next(iterator))

#print(next(iterator))

#print(next(iterator))

#my_list = [4, 7, 0]

#for element in my_list:
#    print(element)


#my_list = [1, 2, 3, 4, 5]


#iterator = iter(my_list)

#for element in iterator:

#    print(element)

#from itertools import count

#infinite_iterator = count(1)

#for i in range(5):
#print(next(infinite_iterator))


#def generator_name(arg):
#    yield something


#def my_generator(n):
#    value = 0
#    while value < n:
#       yield value

#        value += 1

#for value in my_generator(3):
#    print(value)

#generator = my_range(3)
#print(next(generator))
#print(next(generator))
#print(next(generator))

#squares_generator = (i * i for i in range(5))

#for i in squares_generator:
#    print(i)

#def PowTwoGen(max=0):
#    n = 0
#    while n < max:
#        yield 2 ** n
#        n += 1

#def all_even():
#    n = 0
#    while True:
#        yield n
#        n += 2

#def fibonacci_numbers(nums):
#    x, y = 0, 1
#    for _ in range(nums):
#       x, y = y, x+y
#        yield x

#def square(nums):
#    for num in nums:
#        yield num**2

#print(sum(square(fibonacci_numbers(10))))

#def add(x, y):
#    return x + y

#def calculate(func, x, y):
#    return func(x, y)

#result = calculate(add, 4, 6)
#print(result)  # prints 10

#def greeting(name):
#    def hello():
#        return "Hello, " + name + "!"
#    return hello

#greet = greeting("Atlantis")
#print(greet())  # prints "Hello, Atlantis!"

# Output: Hello, Atlantis!