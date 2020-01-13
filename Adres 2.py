s=input("adres :")
a=s.split(":")
for i in a:
    print (i)
n=s.find(":")
name=s[:n]
s=s[n+1:]
n=s.find(":")
name2=s[:n]
s=s[n+1:]
s=name+'\n'+name2+'\n'+s
print(s)
