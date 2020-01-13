import math as m
x=int(input("x="))
y=int(input("y="))
z=int(input("z="))
l=0.5*x**6+3*m.cos(x+y)+m.pow(m.e,-0.1*y*z)-m.sqrt(m.fabs(x*y))
print("l=",l)
