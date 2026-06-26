def rotate_array(arr):
    return [arr[-1]] + arr[:-1:]
num=list(map(int,input("enter the elements of list ").split()))
print(rotate_array(num))