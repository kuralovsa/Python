import math as m
k=int(input("k:"))
n=int(input("n:"))
def almas():
    A=m.factorial(k)/m.factorial(n-k)
    print("A=",A)
def teru():
    C=m.factorial(n)/m.factorial(n-k)*m.factorial(k)
    print("C=",C)
def orn():
    O=m.factorial(n)
    print("Oryn",O)
almas()
teru()
orn()
