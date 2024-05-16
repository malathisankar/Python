def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

input = input("Enter a no: ")
if is_palindrome(input):
    print(input, "is a palindrome.")
else:
    print(input, "is not a palindrome.")
