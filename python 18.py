import math as m
n=int(input('n='))
res=0
for i in range(n):
    res=m.sqrt(3*(i-1)+m.sqrt(3*n)+res)
    i+=1
print("res=",res)
