import math
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
if(a>=b and b>=c):
    print("a=",a*2,"b=",b*2,"c=",c*2)
else:
    print(abs(a),abs(b),abs(c))
