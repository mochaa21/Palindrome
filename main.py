def palindrome(array):
    kiri = 0
    kanan = len(array) - 1
    for _ in array:
        if array[kiri] == array[kanan]:
            kiri += 1
            kanan -= 1
            if array[kiri] == array[kanan]:
                return f"This is palindrome. Text: {array}"
    return f"This is not a palindrome. Text: {array}"


array = ['M', 'A', 'L', 'A', 'M']
array_2 = ['B', 'U', 'K', 'U']
array_3 = ['R', 'A', 'D', 'A', 'R']
print(palindrome(array))
print(palindrome(array_2))
print(palindrome(array_3))