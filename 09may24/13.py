n=int(input())
p=0
i=2
while (i < n):
    if (n%i == 0):
       p += 1
    i += 1
if (p == 0):
  print("This number is prime")
else:
  print("This number is not prime")

