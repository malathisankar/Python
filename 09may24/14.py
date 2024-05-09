for n in range(10,20):
    for i in range(2,n):
     if n%i == 0:
          j = n/i
          print("%d equals to %d * %d",(n,i,j))
          break
     else:
          print("This is prime no")
          break
