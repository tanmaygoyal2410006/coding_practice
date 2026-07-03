def subarray(arr):
    n = len(arr)
    sums = []
    
    for i in range(n):
        sum= 0
        temp = []
        for j in range(i, n):
            temp.append(arr[j])
            sum+= arr[j]
            print(temp)
            sums.append(sum)
    print(sums)   

    max = sums[0]
    for i in range(len(sums)):
        if sums[i] > max:
            max = sums[i]

    print(max)    
arr=[1,2,3,4,5]    
result= subarray(arr)
print(result)





