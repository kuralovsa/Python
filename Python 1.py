import math as m
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))

P=a+b+c
p=P/2
s=m.sqrt(p*(p-a)*(p-b)*(p-c))
print("P :" ,P)
print("S :" ,s)
