def selection_sort(arr): 
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if(arr[i]>arr[j]):
                arr[i],arr[j]=arr[j],arr[i]
    return arr
arr=list(map(int,input("enter the elements of list ").split()))
c=selection_sort(arr)
print(c)

            

