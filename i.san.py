from random import*
a=[randint(0,10) for i in range(10)]
l=a
print(l)
n=int(input("i.s:"))
for i in l:
    if (l[i]==n):
        print('A[',i,']=',n)
    else:
        print('is not a')
        
        
        
