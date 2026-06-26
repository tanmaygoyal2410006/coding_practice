def merge(lst1, lst2):
    lst3 = lst1 + lst2
    result = []
    for i in lst3:
        if i not in result:
            result.append(i)
    return result
a = [ 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]
print(merge(a, b))