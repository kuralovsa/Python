import math as m
c=int(input("c="))
x=int(input("x="))
y=int(input("y="))
b=c*((y+x**2)**1/2)*(m.cos(x)-(m.fabs(c-y)))
print("b=",b)
