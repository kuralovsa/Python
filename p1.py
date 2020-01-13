import math as m
a=int(input('a='))
n=int(input('n='))
res=1
for i in range(n):
    res=a*(a+res)
    i+=1
print("res=",res)
