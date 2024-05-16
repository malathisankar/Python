#user_input = input("Enter a string: ")
#cleaned_string = ''.join(filter(str.isalpha, user_input))
#print("String after removing non-alphabetic characters:", cleaned_string)


s=input("Enter a string: ")
s1=" ".join(c for c in s if c.isalpha())
print(s1)
