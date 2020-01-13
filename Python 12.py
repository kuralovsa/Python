import math as m
x=int(input("x="))
y=int(input("y="))
z=int(input("z="))
h=2+x**2/m.sqrt(2)+m.fabs(y**3)/m.sqrt(3)+(z**4*(m.log(x,m.e)+1)*m.sqrt(2))/m.sqrt(4)
print("h=",h)
