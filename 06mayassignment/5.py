n=int(input("Enter a number : "))
a=n
rn=0
while ( n > 0):
    b=n%10
    rn=rn*10+b
    n=n//10
if a==rn:
    print("It is palindrome : ",a)
else: 
    print("It is not a palindrome : ",a)
 
