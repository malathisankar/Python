#input = input("Enter a string: ")
#d = ''.join(sorted(set(input), key=input.index))
#print("String after removing duplicates:", d)


input = input("Enter a string: ")
p=""
for char in input:
    if char not in p:
        p=p+char
print(p)
k=list(" ")
