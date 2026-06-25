""""
num=list(input("enter the elements of list ").split())
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i]<num[j]:
            num[i],num[j]=num[j],num[i]
print("the longest element in the list is:",num[0])
"""

words = ["apple", "banana", "mango", "watermelon", "kiwi"]

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print(longest)