input = "abcba"


def is_palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return is_palindrome(string[1:-1]) #문자열의 시작과 끝을 제외하고 재귀

print(is_palindrome(input))