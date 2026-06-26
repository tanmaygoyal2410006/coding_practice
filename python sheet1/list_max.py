num=list(map(int,input("enter the elements of list ").split()))
max=num[0]
for i in range (0,len(num)):
    if num[i] > max :
        max=num[i]
print(max)        