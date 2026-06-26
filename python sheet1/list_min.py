num=list(map(int,input("enter the elements of list ").split()))
min=num[0]
for i in range (0,len(num)):
    if num[i] < min:
        min=num[i]
print(min)        