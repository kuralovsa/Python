from random import*
n=int(input('kolishestva chisel='))
s=[randint(0,100)  for i in range(n)]
if(s<50):
    l=sum(s)
    print(l)
elif(s>50):
    k=sum(s)
    print(k)
