arr = [1, 2, 3, 4, 5]
i = len(arr) - 1   
j = i - 1          
while j >= 0:
    arr[i], arr[j] = arr[j], arr[i]
    i -= 1
    j -= 1
print(arr)