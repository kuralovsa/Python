l=['alma',2,4,6,5.6,7.8,'ananas']


intte=list(filter(lambda x:   type(x)==int ,l))
floattar=list(filter(lambda x: type(x)==float,l))
strler=list(filter(lambda x: type(x)==str,l))

print(intte)
print(floattar)
print(strler)
