def f():
    for jol in range(6):
        for bagan in range(5):
            if(jol==0 and (bagan>=0 and bagan<5)) or\
                    (jol==1 and bagan==0) or\
                    (jol==2 and bagan==0)or\
                    (jol==3 and (bagan>=0 and bagan<5)) or\
                    (jol==4 and bagan==0) or\
                    (jol==5 and bagan==0):
                print('F',end=' ')
            else:
                print(" ", end=" ")
        print()
def I():
    for row in range(7):
        for column in range(3):
            if column == 1 or row == 0 or row == 6:
                print("I", end=" ")
            else:
                print(" ", end=" ")
        print()

def N():
    for row in range(7):
        for column in range(7):
            if row == column or (column == 0 and row != 0) \
                    or column == 6 and row != 6:
                print("N", end=" ")
            else:
                print(" ", end=" ")
        print()
def i():
    for j in range(6):
        for b in range(5):
            if(j==0 and (b>=0 and b<5)) or\
                    (j==1 and b==2) or\
                    (j==2 and b==2) or\
                    (j==3 and b==2) or\
                    (j==4 and b==2) or\
                    (j==5 and (b>=0 and b<5)):
                print('I',end=' ')
            else:
                print(" ", end=" ")
        print()
def one():
    for row in range(7):
        for column in range(3):
            if ((row >= 0 and row <= 2) and row + column == 2) \
                    or column == 2 and row != 0:
                print("1", end=" ")
            else:
                print(" ", end=" ")
        print()
print("I:")
i()
N()
print("F:")
f()
print("1:")
one()
print('')
one()
