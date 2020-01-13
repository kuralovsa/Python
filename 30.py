s=input("Soz: ")
soz=s.split()
n=len(soz)
print(soz)
for i in range(n):
    if len(soz[0])<len(soz[i]):
        h=soz[i]
        n=i
print("En uzyn soz: ",h)
print("En uzyn soz id: ",n)
    
