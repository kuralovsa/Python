from random import*
n=int(input("n=")
l=[randint(1,5) for i in range(n)]
print("generatsyalangan tizim=",l)

En_kop_san=None
kop_san_sani=0
set_l=set(l)
	  
for i in set_l: 
	  sani=l.count(i)
	  if sani>kop_san_sani:
	  		kop_san_sani=sani
	  		En_kop_sani=i
print(f'En kop kaytalangan san={En_kop_san}, count={kop_san_sani}')
