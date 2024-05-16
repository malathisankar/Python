string=input("Enter string: ")
count=0
temp=[]
for i in string:
    if(i not in temp):
        count+=1
        temp.append(i)
print('Total Unique Characters count:',count)    
