from random import*
a=[randint(0,10) for i in range(10)]
l=a
print(l)
for i in l:
    if l[i]==l[i+1]:
        print(l[i])
        continue
    else:
        break
