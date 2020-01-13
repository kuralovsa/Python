from my_func import*
l=['alma',2,4,6,5.6,7.8,'ananas']
print(l)
intter= list(my_map(lambda x:   type(x)==int ,l))
floattar=list(my_map(lambda x: type(x)==float,l))
strler=list(my_map(lambda x: type(x)==str,l))

print(intter)
print(floattar)
print(strler)
