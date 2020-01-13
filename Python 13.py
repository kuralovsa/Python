import math as m
x=int(input("x="))
y=int(input("y="))
z=int(input("z="))
i=(1+y)*(m.sin(z)**2)**1/2-m.fabs(y-x)/5
print("i=",i)
