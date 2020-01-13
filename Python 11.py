import math as m
x=int(input("x="))
y=int(input("y="))
g=(1+m.cos(x+y))*x**3/m.fabs(m.e**x-2*y/(1+m.pow(x*y,2)))+m.asin(y)
print("g=",g)
