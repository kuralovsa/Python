a=[i for i in range(1,50000)]
count=0
k=input(a)
l=k.split()
for i in l:
    s=l[i].split()
    h=len(l[i])
    
    if (s==[2]):
        count+=1
print(count)