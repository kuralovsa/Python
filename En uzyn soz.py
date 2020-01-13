soz=input("Sozdi engiz=")
print(soz) 
n=soz.split()
print(n) 

idUzin=0

for i in range(1,len(n)):
	if len(n[iduzin])<len(n[i]):
		idUzin=i
print(f"Jazilgan soz iwinde en uzin soz={n[idUzin], uzindigi={idUzin"}
