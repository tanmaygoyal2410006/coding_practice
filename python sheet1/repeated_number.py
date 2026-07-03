def repeat_n2(arr):
    n=len(arr)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                return arr[i]

def repeat_n(arr):
    n=len(arr)
    sum=0
    for i in range(0,n):
        sum+=arr[i]
    a=int(((n-1)*n)/2)
    b=sum-a
    return b 
                  
lst=[1,2,3,4,2]
result=repeat_n(lst)
print(result)

            
