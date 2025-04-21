def is_palindrome(input_string: str) -> bool:
    if not input_string:  # Якщо рядок порожній
        return True
    if len(input_string) == 1:  # Якщо тільки один символ
        return True
    if input_string[0] != input_string[-1]:  # Перевіряємо перший і останній символ
        return False
    return is_palindrome(input_string[1:-1])  # Рекурсія для скороченого рядка


print("is_palindrome('madam'):", is_palindrome("madam"))
print("is_palindrome('apple'):", is_palindrome("apple"))
print("is_palindrome(''):", is_palindrome(""))
print("is_palindrome('a'):", is_palindrome("a"))


from typing import Union, List

def sum_list(num: List[Union[int, float, list]]) -> Union[int, float]:
    try:
        if not isinstance(num, list):
            raise TypeError("Помилка: Введіть список.")

        total = 0
        for item in num:
            if isinstance(item, list):
                total += sum_list(item)  # Рекурсивний виклик для вкладених списків
            elif isinstance(item, (int, float)):  # Якщо це число
                total += item
            else:
                raise ValueError("Помилка: Список містить некоректний елемент.")
        return total
    except TypeError as e:
        print(e)
        return 0
    except ValueError as e:
        print(e)
        return 0



print("sum_list([1, [10, [5, 8], 4], 7]):", sum_list([1, [10, [5, 8], 4], 7]))
print("sum_list([1, [10, 'string', 5], 7]):", sum_list([1, [10, 'string', 5], 7]))

def contains(element: Union[int, str], num: List[Union[int, str, list]]) -> bool:
    try:
        if not isinstance(num, list):
            raise TypeError("Помилка: Введіть список.")

        for item in num:
            if isinstance(item, list):
                if contains(element, item):  # Рекурсивний виклик для вкладених списків
                    return True
            elif item == element:  # Якщо знайшли потрібний елемент
                return True
        return False
    except TypeError as e:
        print(e)
        return False

