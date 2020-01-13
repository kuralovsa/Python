from random import*
b=[randint(1,3) for i in range(1)]
print("Tas,kaishy,kagaz oynaiyk: ",'\n 1.Tas','\n 2.Kaishy','\n 3.Kagaz')
k=int(input("1 men 3 arasynan birin tandanyz: "))
n=[]
n.append(k)
a=(b)
if a==n:
    print("Zhenis zhok") 
elif n==[1] and a==[2]:
    print('Syz zhendiniz')
elif n==[1] and a==[3]:
    print('II zhendi')
elif n==[2] and a==[1]:
    print('II zhendi')
elif n==[2] and a==[3]:
    print('Syz zhendiniz')
elif n==[3] and a==[1]:
    print('Syz zhendiniz')
elif n==[3] and a==[2]:
    print('Syz zhendiniz')
else:
    print('Birdene durys emes')
print("Syzdin tandauynyz: ",n,"II tandauy",a)