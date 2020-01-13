from my_func import*
L1=[12,23,34]
L2=[11,43,33]
L3=[2,4,5]
arr=[x+y+z for (x,y,z) in zip(L1,L2,L3)]
print(arr)
s=map(lambda x,y,z: x+y+z,L1,L2,L3)
print(list(s))

a=[1,2,3,4]
b=[11,33,44,55]
ab=[a[i]+b[i] for i in range(len(a))]
print(ab)


