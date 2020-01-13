import random  
vvod = input('Введите любое число:')
n = int(vvod)
a=[random.randint(0,100) for i in range(n)]
m=int(input('Chyslo poyska: '))
try:
    if n < m:
        raise TypeError ('Id ne nayden ')
    if n >m:
        raise IndexError ('ERROR')
    if n<=m:
        raise StopIteration('Id ne nayden ')
except TypeError :
    print('Id ne nayden')
except IndexError :
    print('ERROR')
except StopIteration :
    print('Id ne nayden ')
    
