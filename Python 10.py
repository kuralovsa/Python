import math as m
x=int(input("x="))
y=int(input("y="))
z=int(input("z="))
t=x+(m.fabs(x)+m.e**y)**1/2-(z**3*m.sin(y)**2)/(y+z**2/(y-x))
print("t=",t)
