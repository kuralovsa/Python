import math as m
x=int(input("x="))
y=int(input("y="))
z=int(input("z="))
e=((m.cos(x)-m.sin(y))**3)/m.tan(x)**1/2+m.log(x*y*z,m.e)**2
print("e=",e)
