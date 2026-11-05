# Palindrome checker (functions)
def is_palindrome(word):
    corrected_word = word.lower()
    return corrected_word == corrected_word[::-1]
print(f'is_palindrome("level") -> {is_palindrome("level")}')
print(f'is_palindrome("python") -> {is_palindrome("python")}')
print(f'is_palindrome("Level") -> {is_palindrome("Level")}')  
print(f'is_palindrome("radar") -> {is_palindrome("radar")}')