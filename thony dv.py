from random import*
print('*** Welcome to CASINO VEGAS ***')
print('If you want play '+"Void 1\t"+'To close'+'Void 2')
k=int(input())
if k==1:
    print('Please select "COEFFICIENT" wish you want!')
    print('You have 5 kind of "COEFFICIENT":')
    print("1.'1.2%'")
    print("2.'1.4%'")
    print("3.'1.6%'")
    print("4.'1.8%'")
    print("5.'2.0%'")
    print('Please select your "COEFFICIENT"')
    r=int(input())
    if r==1:
        print("Your 'COEFFICIENT' 1.2%: ")
        print("Please ENTER the sum of your money:")
        h=int(input())
        print("Select one number from 1 to 20: ")
        a=[randint(1,10) for i in range(1)]
        n=int(input())
        l=[]
        l.append(n)
        if a==l:
            print("You winner :-) !!!"+"The amount of your winning: "+str(h*1.2))
            print("!!!CONGRATULATIONS!!!")
            print("Want to play yet")
            print('1. Yes\t'+'2. No')
            b=int(input())
            if b==1:
                pass
            elif b==2:
                pass
            else:
                print("Something went wrong")
        elif a!=l:
            print("You lost :-("+str(a))
            print("Want to play yet")
            print('1. Yes\t'+'2. No')
            b1=int(input())
            if b1==1:
                pass
            elif b1==2:
                pass
            else:
                print("Something went wrong")
        else:
            print("Something went wrong")
    elif r==2:
        print("Your 'COEFFICIENT' 1.4%:")
        print("Please ENTER the sum of your money:")
        h1=int(input())
        print("Select one number from 1 to 40: ")#1 in 40 nambers
        a1=[randint(1,40) for i in range(1)]
        n1=int(input())
        l1=[]
        l1.append(n1)
        if a1==l1:
            print("You winner :-) !!!"+"The amount of your winning: "+str(h*1.4))#возврошаем сумму денег в str
            print("!!!CONGRATULATIONS!!!")
            print("Want to play yet")
            print('1. Yes\t'+'2. No')
            b3=int(input())
            if b3==1:
                pass #возвращаем 
            elif b3==2:
                pass
            else:
                print("Something went wrong")
        elif a1!=l1:
            print("You lost :-("+str(a1))
            print("Want to play yet")
            print('1. Yes\t'+'2. No')
            b4=int(input())
            if b4==1:
                pass
            elif b4==2:
                pass
            else:
                print("Something went wrong")
        else:
            print("Something went wrong")
    elif r==3:
        print("Your 'COEFFICIENT' 1.6%:")
        print("Please ENTER the sum of your money:")
        h2=int(input())
        print("Select one number from 1 to 60: ")#1 in 40 nambers
        a2=[randint(1,40) for i in range(1)]
        n2=int(input())
        l2=[]
        l2.append(n2)
        if a2==l2:
            print("You winner :-) !!!"+"The amount of your winning: "+str(h*1.6))
            print("!!!CONGRATULATIONS!!!")
            print("Want to play yet")
            print('1. Yes\t'+'2. No')
            b5=int(input())
            if b5==1:
                pass
            elif b5==2:
                pass
            else:
                print("Something went wrong")
        elif a2!=l2:
            print("You lost :-("+str(a1))
            print("Want to play yet")
            print('1. Yes\t'+'2. No')
            b6=int(input())
            if b6==1:
                pass
            elif b6==2:
                pass
            else:
                print("Something went wrong")
        else:
            print("Something went wrong")
    if r==4:
        print("Your 'COEFFICIENT' 1.8%:")
        print("Please ENTER the sum of your money:")
        h3=int(input())
        print("Select one number from 1 to 80: ")#1 in 40 nambers
        a3=[randint(1,40) for i in range(1)]
        n3=int(input())
        l3=[]
        l3.append(n3)
        if a3==l3:
            print("You winner :-) !!!"+"The amount of your winning: "+str(h*1.8))
            print("!!!CONGRATULATIONS!!!")
            print("Want to play yet")
            print('1. Yes\t'+'2. No')
            b7=int(input())
            if b7==1:
                pass
            elif b7==2:
                pass
            else:
                print("Something went wrong")
        elif a3==l3:
            print("You lost :-("+str(a3))
            print("Want to play yet")
            print('1. Yes\t'+'2. No')
            b8=int(input())
            if b8==1:
                pass
            elif b8==2:
                pass
            else:
                print("Something went wrong")
        else:
            print("Something went wrong")
    if r==5:
        print("Your 'COEFFICIENT' 2.0%:")
        print("Please ENTER the sum of your money:")
        h4=int(input())
        print("Select one number from 1 to 80: ")#1 in 40 nambers
        a4=[randint(1,40) for i in range(1)]
        n4=int(input())
        l4=[]
        l4.append(n4)
        if a4==l4:
            print("You winner :-) !!!"+"The amount of your winning: "+str(h*2))
            print("!!!CONGRATULATIONS!!!")
            print("Want to play yet")
            print('1. Yes\t'+'2. No')
            b9=int(input())
            if b9==1:
                pass
            elif b9==2:
                pass
            else:
                print("Something went wrong")
        elif a4!=l4:
            print("You lost :-("+str(a4))
            print("Want to play yet")
            print('1. Yes\t'+'2. No')
            b11=int(input())
            if b11==1:
                pass
            elif b11==2:
                pass
            else:
                print("Something went wrong")
        else:
            print("Something went wrong")
if k==2:
    pass
else:
    print('Please void "intenger"!')
    print("Want to play yet")
    print('1. Yes\t'+'2. No')
    
