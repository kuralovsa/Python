import math as m
h=int(input("h="))
a=m.sqrt((m.fabs(m.sin(8*h))+17)/(1-m.sin(4*h)*m.cos(h**2+18))**2)
b=1-m.sqrt(3/3+m.fabs(m.tan(a*h**2)-m.sin(a*h)))
c=a*h**2-m.sin(b*h)+b*h**3*m.cos(a*h)
d=b**2-4*a*c
print("a=",a,"b=",b,"c=",c,"d=",d)
if(d>=0):
    x1=b-m.sqrt(d)/2*a
    x2=b+m.sqrt(d)/2*a
    print(x1,x2)
else:
    print("x1,x2 jok")

