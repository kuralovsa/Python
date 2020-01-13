from random import*
a=[randint(0,10) for i in range(10)]
l=a
k=0
print(l)
n=int(input("i.s:"))
for i in l:
    if l[i]==n:
        k+=1
        print(n,k)
        continue
    else:
        print('is not a')
