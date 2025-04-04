#num1 = 5
#print(num1, 'is of type', type(num1))

#num2 = 5.42
#print(num2, 'is of type', type(num2))

#num3 = 8+2j
#print(num3, 'is of type', type(num3))

#num1 = int(2.3)
#print(num1)

#num2 = int(-2.8)
#print(num2)

#num3 = float(5)
#print(num3)

#num4 = complex('3+5j')
#print(num4)

#import random

#print(random.randrange(10, 20))

#list1 = ["a", "b", "c", "d", "e"]

#print(random.choice(list1))

#random.shuffle(list1)
#print(list1)

#print(random.random())

#print(math.pi)

#print(math.cos(math.pi))

#print(math.exp(10))

#print(math.log10(1000))

#print(math.sinh(1))
#print(math.factorial(6))


#import math

#def calculete_area(radius1):
#    perimetr = math.pi * radius1**2
#    return round(perimetr, 2)

#radius = 5

#print(calculete_area(radius))

#LIST

#ages = [19, 26, 29]
#print(ages)

#student = [ "Jack", 32, "Computer Science", [2, 4]]
#print(student)

#empty_list = []
#print(empty_list)

#languages = ["Python", "Swift", "C++"]
#print("languages[0] =", languages[0])

#print("languages[2] =", languages[2])

#print("languages[-1] =", languages[-1])

#print("languages[-3] =", languages[-3])

#my_list = ["p", "r", "o", "g", "r", "a", "m"]
#print("my_list =", my_list)

#print("my_list[2: 5] =", my_list[2: 5])

#print("my_list[2: -2] =", my_list[2: -2])

#print("my_list[0: 3] =", my_list[0: 3])

#print("my_list[5: ] =", my_list[5: ])

#print("my_list[: -4] =", my_list[: -4])

#print("my_list[:] =", my_list[:])

#fruits = ["apple", "banana", "orange"]
#print("Original List:", fruits)

#fruits.append("cherry")
#fruits.insert(2, "cherry")

#print("Updated List:", fruits)

#numbers = [1, 3, 5]
#print("Numbers:", numbers)

#even_numbers = [2, 4, 6]
#print("Even numbers:", even_numbers)

#numbers.extend((even_numbers))

#print("Updateed Numbers:", numbers)

#colors = ["Red", "Black", "Green"]
#print("Original List:", colors)

#colors[2] = "Purple"

#colors[2] = "Blue"

#print("Updated List:", colors)

#numbers = [2,4,7,9]

#numbers.remove(4)

#print(numbers)
#names = ["John", "Eva", "Laura", "Nick", "Jack"]

#del names[1]
#print(names)

# names[1: 3]
#print(names)

#cars = ["BMW", "Mercedes", "Tesla"]

#print("Total Elements:", len(cars))

#fruits = ["apple", "banana", "orange"]

#for fruit in fruits:
#    print(fruit)

#def find_largest(numbers):
#    if numbers1 == 9:
#        return 9

#    return 9

#umbers1 = [1, 2, 9, 4, 5]

#print(find_largest(numbers1))

#TUPLE

#numbers = (1, 2, -5)
#print(numbers)

#language = ("Python", "Swift", "C++")

#print(language[0])

#print(language[2])

#cars = ("BMW", "Tesla", "Ford", "Toyota")
#print("Total Items:", len(cars))

#def modify_tuple(tuples, element):
#    element = list(tuples)
#    element.append(4)
#    return element

#result = modify_tuple((1, 2, 3), 4)
#print(result)

#SETS

#student_id = {112, 114, 116, 118, 115}
#print("Student ID:", student_id)

#vowel_letters = {"a", "e", "i", "o", "u"}
#print("Vowels Letters:", vowel_letters)

#mixed_set = {"Hello", 101, -2, "Bye"}
#print("Set of mixed data types:", mixed_set)

#empty_set = set()

#empty_dictionary = { }

#print("Data type of empty_set:", type(empty_set))

#print("Data type of empty_dictionary:", type(empty_dictionary))

#numbers = {2, 4, 6, 6, 2, 8}
#print(numbers)

#numbers = {21, 34, 54, 12}

#print("Initial Set:", numbers)

#numbers.add(32)

#print("Updated Set:", numbers)

#companies = {"Lacoste", "Ralph Lauren"}
#tech_companies = ["apple", "google", "apple"]

#companies.update(tech_companies)
#print(companies)

#languages = {"Swift", "Java", "Python"}

#print("Initial Set:", languages)

#removedValue = languages.discard("Java")

#print("Set after remove():", languages)

#A = {2, 3, 5}

#B = {1, 2, 6}

#print("Intersection using &:", A & B)

#print("Intersection():", A.intersection(B))

#print("Difference using &:", A - B)

#print("Difference using difference():", A.difference(B))

#print("Using ^:", A ^ B)

#print("Using symmetric_difference():", A.symmetric_difference(B))

#def identical_items ( set1, set2 ):
#    return set1 & set2

#result = identical_items( {1, 2, 3, 4}, {3, 4, 5, 6})
#print(result)

#DICTIONATY

#country_capitals = {
#    "Germany": "Berlin",
#    "Canada": "Ottawa",
#    "England": "London"
#}

#print(country_capitals)

#print(country_capitals["Germany"])
#print(country_capitals["England"])

#country_capitals["Italy"] = "Rome"

#print(country_capitals)

#del country_capitals["Germany"]

#print(country_capitals)


#print(country_capitals)

#country_capitals["Germany"] = "France "

#print(country_capitals)

#for country in country_capitals:
#    print(country)


#for country in country_capitals:
#    capital = country_capitals[country]
#    print(capital)

#file_types = {
#    ".txt": "Text File",
#    ".pdf": "PDF Dicument",
#    ".jpg": "JPEG Image",
#}

#print(".pdf" in file_types)
#print(".mp3" in file_types)
#print(".mp3" not in file_types)

#def merge_dictionaries (dict1, dict2):
#    return dict1 | dict2

#dict1 = {"one": "Nikita",
#         "second": "Klimchuk"
#}

#dict2 = {"1": "Ivan",
#         "2": "Shevchuk"
#         }
#result = merge_dictionaries(dict1, dict2)
#print(result)














