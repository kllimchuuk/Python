number = 10

# assign value to site_name variable
#site_name = 'programiz.pro'

#print(site_name)

# Output: programiz.pro

# assigning a new value to site_name
#site_name = 'apple.com'

#print(site_name)

#a, b, c = 5, 3.2, 'Hello'

#print(a) #prints 5
#print(b) #prints 3.2
#print(c) #prints 'Hello'

#site1 = site2 = 'programiz.com'

#print (site1) # prints programiz.com
#print (site2) # prints programiz.com

# logic literals

#is_pass = True
#print(is_pass)

# character literals
#some_character = 's'

#special literals
#value = None
#print(value)

# list literal
#fruits = ["apple", "mango", "orange"]
#print(fruits)

# tuple literal
#numbers = (1, 2, 3)
#print(numbers)

# dictionary literals
#alphabets = {'a':'apple', 'b':'ball', 'c':'cat'}
#print(alphabets)

# set literal
#vowels = {'a', 'e', 'i', 'o', 'u'}
#print(vowels)

# Transformation integer in float

#integer_number = 123
#loat_number = 1.23

#new_number = integer_number + float_number
#print("Value:",new_number)
#rint("Data Type:",type(new_number))

# Explicit Type Conversion
#num_string = '12'
#num_integer = 23

#print("Data type of num_string before Type Casting:", type(num_string))

# explicit type conversion
#num_string = int(num_string)

#print("Data type of num_string after Type Casting:", type(num_string))

#num_sum = num_integer + num_string

#print("Sum:", num_sum)
#print("Data type of num_sum:", type(num_sum))

# print with end whitespace
#print('Good Morning!', end= ' ')

#print('It is rainy today')

# parameters sep

#print('New Year', 2023, 'See you soon!', sep= '. ')
#number1 = -10.6
#name = "Programiz"

#print(5)
#print(number1)
#print(name)

#print('Programiz is ' + 'awesome.')

#x = 5
#y = 55
#print('The value of x is {} and y is {}'.format(x, y))

# Input
# using input() to take user input
#num1 = int(input('Enter a number: '))

#print('You Entered:', num1)
#print('Data type of num1:', type(num1))

#a = 5
#b = 6

#print((a > 2) and (b >= 6))

#x1 = 5
#y1 =5
#x2 = 'Hello'
#y2 = 'Hello'
#x3 = [1, 2, 3]
#y3 = [1, 2, 3]

#print(x1 is not y1)
#print(x2 is y2)
#print(x3 is y3)

#message = 'Hello world'
#dict1 = {1:'a', 2:'b'}

#print('H' in message)
#print('hello' not in message)
#print(1 in dict1)
#print('a' in dict1)

#def split_bill(subtotal: float, friends: int) -> float:
#    if friends <= 0:
#        raise ValueError("Кількість друзів має бути більшою за нуль.")

#    total = subtotal * 1.2 # Додаємо 20 відсотків
#    per_person = total / friends
#    return round(per_person, 2)

#subtotal_amount = 100.0
#num_friends = 4

#amount_per_person = split_bill(subtotal_amount, num_friends)
#print(f"Кожен друг повинен заплатити: {amount_per_person} грн")