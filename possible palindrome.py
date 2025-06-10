def is_palindrome(word):
    reversed_word = ""
    for char in word:
        reversed_word = char + reversed_word
    if word == reversed_word:
        return True
    else:
        return False
print(is_palindrome("madam"))
print(is_palindrome("racecar"))
print(is_palindrome("hello"))
