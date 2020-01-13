import random
def creatArray():
    r=0
    print("Input first index matrix")
    x = int(input())
    print("Input second index matrix")
    y = int(input())
    array=[]
    #1
    for i in range (x):
        array.append([])
        for j in range(y):
            array[i].append(random.randint(0,100))
            r+=1
    #2
    print("Matrix:")
    for u in range(x):
        print(array[u])
    
    #3
    colmn = 0
    colmnIter = 1
    maxm = 0
    for n in range(y):
        s=0
        for m in range(x):
            s+=array[m][n]
        print("%3d" % (s), end=' ')
        
        if(maxm<s):
            maxm=s
            colmn+=colmnIter
        else:
            colmnIter +=1
        
    print("\nМаксимальный столб имеет сумму: %3d\nИ этот столбец под номером %2i" % (maxm, colmn))
