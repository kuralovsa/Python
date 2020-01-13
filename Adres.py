s=input("adres :")
n=s.find("/")
name=s[:n]
s=s[n+1:]
n=s.find("/")
name2=s[:n]
s=s[n+1:]
n=s.find("/")
name3=s[:n]
s=s[n+1:]
n=s.find("/")
name4=s[:n]
s=s[n+1:]
s=name+'\n'+name2+'\n'+name3+'\n' +name4+'\n'+s
print(s)
