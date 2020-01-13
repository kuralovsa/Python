from random import*
n=int(input("n="))
l=[randint(0,15) for i in range(n)]
print("generatsyalangan tizim=",l)      
r=sorted(l, reverse = True)
print("Posle sortirovki:",r)
d=int(input("izdelimdegy san="))
for i in range(n):
    if r[i]==d:
        print("id=",i,"element",d)
    else:
        print("nenaiden!")
