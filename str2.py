s=input("Vyvod :")
s1=""
for c in s:
    if c=="a":
        c="b"
    elif c=="A":
        c="B"
    elif c=="B":
        c="A"
    elif c=="b":
        c="a"
    s1=s1+c
print(s1)
