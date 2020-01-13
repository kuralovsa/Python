import random
k=0
n=int(input('kolichestva chysel: '))
s=[random.randint(0, 100) for i in range(n)]
print('a[i]: ',s)
 
for i in range(0,n):
    for j in range (2,s[i]-1):
        if s[i]%j == 0:
            break
    if j>s[i]/2:
        k=k+1
 
print ('простых чисел:',k)
