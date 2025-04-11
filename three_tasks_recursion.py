# One task

def is_palindrome(s):
    if len(s) <= 1:   # Якщо рядок є порожнім або складається з одного елементу = True
        return True
    if s[0] != s[-1]: # Якщо перший і останій символ не збігаються, то - False
        return False
    return is_palindrome(s[1:-1])  # Рекурсія, яка перевіряє внутрішню частину рядка

print("Palindrome is:", is_palindrome("madam"))
print("Palindrome is:", is_palindrome("apple"))

# Second task

def sum_list(num):
    total = 0
    for item in num:
        if isinstance(item, list): # Якщо елемент є список, то викликаємо функцію рекурсивно
            total += sum_list(item)
        else:
            total += item   # Якщо елемент є число, додаємо до загальної суми
    return total

print("Sum is:", sum_list([1,[10,[5,8], 4], 7]))

# Three task

def contains(element, num):
    for item in num:
        if isinstance(item, list):  # Якщо елемент є списком
            if contains(element, item):  # Перевіряємо список за допомогою рекурсії
                return True
        elif item == element:  # Якщо знайшли потрібний елемент
            return True
    return False

print("Contains is:", contains(55, [11, [25, [36, 4], [99]], 55]))
print("Contains is not:", contains(19, [11, [25, [36, 4], [99]], 55]))
