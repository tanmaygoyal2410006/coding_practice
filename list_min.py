num=list(map(int,input("enter the elements of list ").split()))
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i]>num[j]:
            num[i],num[j]=num[j],num[i]
print("the min element in the list is:",num[0])