#divide_numbers = 7 / 0
#print(divide_numbers)

#print(dir(locals()['__builtins__']))

#try:
#   numerator = 10
#    denominator = 0

#    result = numerator / denominator

#    print(result)
#except:
#    print("Error: Denominator cannot be 0.")


#try:
#    even_numbers = [2,5,6,8]
#    print(even_numbers[5])

#except ZeroDivisionError:
#    print("Denominator cannot be 0.")

#except IndexError:
#    print("Index Out of Bound")

#try:
#    num = int(input("Enter a number: "))
#    assert num % 2 == 0
#except:
#    print("Not an even number!")
#else:
#    reciprocal = 1/num
#    print(reciprocal)

#try:
#    numerator = 10
#    denominator = 0

#    result = numerator/denominator

#    print(result)
#except:
#    print("Error: Denominator cannot be 0.")

#finally:
#    print("This is finally block.")

#class CustomError(Exception):
#    ...
#    pass

#try:
#    ...

#except CustomError:
#   ...

#class InvalidAgeException(Exception):
#    "Raised when the input value is less than 18"
#    pass

#number = 18

#try:
#    input_num = int(input("Enter a number: "))
#    if input_num  < number:
#        raise InvalidAgeException
#    else:
#        print("Eligible to Vote")

#except InvalidAgeException:
#    print("Exception occurred: Invalid Age")


#class SalaryNotInRangeError(Exception):
#    """Exception raised for errors in the input salary.

#    Attributes:
#        salary -- input salary which caused the error
#        message -- explanation of the error
#    """

#    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
#        self.salary = salary
#        self.message = message
#        super().__init__(self.message)


#salary = int(input("Enter salary amount: "))
#if not 5000 < salary < 15000:
#    raise SalaryNotInRangeError(salary)

