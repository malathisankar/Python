n=int(input("Enter no.of subjects: "))
i=1
tm=0
am=0
while ( i <= n):
  m=int(input("Enter marks for subjects : "))
  tm+=m
  am=tm/5
  i+=1
print("Total mark :" ,tm)
print("Average mark: ",am)

