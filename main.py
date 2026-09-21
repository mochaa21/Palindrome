def palindrome(array):
    kiri = 0
    kanan = len(array) - 1
    while kiri < kanan:
        if array[kiri] != array[kanan]:
            return f"This is not a palindrome. Text: {array}"
        kiri += 1
        kanan -= 1
    return f"This is palindrome. Text: {array}"
    


# array = ['M', 'A', 'L', 'A', 'M']
array_2 = ['B', 'U', 'K', 'U']
array_3 = ['R', 'A', 'D', 'A', 'R']
array = input("Use a space to enter a word.\nYour input -> ")
array = array.split()
print(palindrome(array_2))
print(palindrome(array_3))
print(palindrome(array))