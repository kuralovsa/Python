for jol in range(5):
    for bagan in range(5):
        if(jol==0 and (bagan>=0 and bagan<5)) or\
            (jol==1 and bagan==0) or\
            (jol==2 and (bagan>=0 and bagan<5)) or\
            (jol==3 and bagan==0) or\
            (jol==4 and bagan==0):
            print('*',end=' ')
        else:
            print(' ',end=" ")
        
    print('')
