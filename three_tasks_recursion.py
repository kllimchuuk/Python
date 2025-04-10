# One task

def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print("Palindrome is:", is_palindrome("madam"))
print("Palindrome is:", is_palindrome("apple"))

# Second task

def sum_list(num):
    total = 0
    for item in num:
        if isinstance(item, list):
            total += sum_list(item)
        else:
            total += item
    return total

print("Sum is:", sum_list([1,[10,[5,8], 4], 7]))

# Three task

def contains(element, num):
    for item in num:
        if isinstance(item, list):
            if contains(element, item):
                return True
        elif item == element:
            return True
    return False

print("Contains is:", contains(55, [11, [25, [36, 4], [99]], 55]))
print("Contains is not:", contains(19, [11, [25, [36, 4], [99]], 55]))
