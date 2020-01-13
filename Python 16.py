import math as m
x=int(input("x="))
y=int(input("y="))
m=m.sqrt(m.fabs(-3*m.tan(x)*m.log(x**4+y)/m.e**-x+1))
print("m=",m)
