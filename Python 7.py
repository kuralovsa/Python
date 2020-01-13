import math as m
x=int(input("x="))
y=int(input("y="))
b=int(input("b="))
c=m.atan(x)-3/m.e**(x*y)+0.5*m.fabs(x+y)/(x+y)**b
print("c=",c)
