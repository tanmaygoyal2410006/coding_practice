def smallest(arr,k):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr[k-1]
arr = list(map(int, input("Enter numbers: ").split()))
k=int(input("enter the number"))
c=smallest(arr,k)
print(k,"th smallest element in the given array is",c)

# Can be more optimized (How? read different methods)