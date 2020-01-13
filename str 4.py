s=input("A.A.T:")
n=s.find(" ")
name=s[:n]
s=s[n+1:]
n=s.find(" ")
name2=s[:n]
s=s[n+1:]
s=s+" "+name[:2]+"."+name2[0]+"."
print(s)
