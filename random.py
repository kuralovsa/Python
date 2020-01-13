from random import*
n=int(input("n= "))
s=0
a=[randint(0,n) for i in range(n)]
for i in a:
    if (i%i==0) and (i/1==i):
        s+=i
        print('sum=',s)
    else:
        print("таких чисел нет")
print('massiv a=',a)
