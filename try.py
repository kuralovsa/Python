import random 
a=[random.randint(1,20) for i in range(1)]
#l=[j for j in range('A','Z')]
n = int(input('Введите любое число:'))
if a == n :
    print('Число наиденно:',a)
else:
    print('Число не совподает:',a,n)
try:
    if n < 0:
        raise TypeError ('Число меньше нуля')
    if n > 10:
        raise IndexError ('Число больше десяти')
except TypeError :
    print('Число меньше нуля')
except IndexError :
    print('Число больше десяти')
except ValueError :
    print('Str not int')