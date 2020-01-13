import math as m
x=int(input("x="))
y=int(input("y="))
a=m.log(y**-(m.fabs(x))**1/2)*(m.sin(x)+m.e**(x+y))
print("a=",a)
