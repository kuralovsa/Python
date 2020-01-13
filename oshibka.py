import random 
a=random.randint(1,20,1)
n = int(input('Введите любое число:'))
if a == n :
    print('Число наиденно:',a)
else:
    print('Число не совподает:',a)
try:
    if n < 0:
        raise TypeError ('Число меньше нуля')
    if n > 10:
        raise IndexError ('Число больше десяти')
    if n % 2 == 0:
        raise ValueError ('Число четное')
except TypeError :
    print('Число меньше нуля')
except IndexError :
    print('Число больше десяти')
except ValueError :
    print('Число четное')


