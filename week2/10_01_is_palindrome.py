input = "abcba"


def is_palindrome(string):
    n = len(string) - 1
    for i in range(n):
        if string[i] != string[n-i]:
            return False
    return True




print(is_palindrome(input))