def check(a,b):
    c=list(str(a))    
    d=list(str(b))
    if c[-1]>d[-1]:
        return c[-1]
    else:
        return d[-1]    
a=int(input("enter a number "))     
b=int(input("enter a number "))  
result=check(a,b)         
print(result)