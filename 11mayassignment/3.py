#user_input = input("Enter a string: ")
#words = user_input.split()
#num_words = len(words)
#print("Number of words in the string:", num_words)


string = input("Enter string = ")
words = string.split()
count = 0
for word in words:
    count += 1
print(count)
