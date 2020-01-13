def my_enumarete(my_list):
    kol = 0
    for i in my_list:
        yield(kol,i)
        kol += 1
if __name__ == "__main__":
    l=[2,4,6,8,9,]
    for i,j in my_enumarete(l):
        print(i,j**3)
#def my_enum(My_list):
    
    
