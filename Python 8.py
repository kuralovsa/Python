import math as m
x=int(input("x="))
y=int(input("y="))
z=int(input("z="))
d=m.pow(m.e,m.fabs(x-y)*m.tan(z))/m.atan(y)+m.sqrt(x)+m.log(x,m.e)
print("d=",d)
