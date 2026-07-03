def minimize_height(arr, k):
    for i in range(len(arr)):
        if i == 0:
            arr[i] += k
        else:
            arr[i] -= k
    arr.sort()
    length=len(arr)
    diff=arr[length-1]-arr[0]
    return diff
num=list(map(int,input("enter the elements of list ").split()))
k=int(input("enter a number"))
result=minimize_height(num,k)
print(result)

