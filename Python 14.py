import math as m
x=int(input("x="))
y=int(input("y="))
z=int(input("z="))
k=m.log(m.fabs((y-m.sqrt(m.fabs(x)))*(x-y*z+x**2/4)),m.e)
print("k=",k)
