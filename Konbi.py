n=int(input("n="))
k=int(input("n="))
def F(san):
    f=1
    for i in range(1,san+1):
        f*=i
    return f
def almas():
    A=F(n)/F(n-k)
    print("A",A)
    
def teru():
    C=F(n)/F(n-k)*F(k)
    print("C=",C)
    
def orn():
    O=F(n)
    print(O)
almas()
teru()
orn()
