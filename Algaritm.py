a=int(input("a="))
b=int(input("a="))
if (a!=0&b!=0):
    if(a>b):
        a=a%b
        print(a)
    else:
        b=b%a
        print(b)
else:
    print(a+b)
