def function(*numbers,flag):
    if flag:
        return list_num1
        print(function)
    else:
        return list_num2
    print(function)
def function1(*numbers,flag):
    list_num1 = []
    if flag==False:
        for number in numbers:
            if number % 2 == 0:
                list_num1.append(number)
    return list_num1

def function2(*numbers,flag):
    list_num2 = []
    if flag==True:
        for number1 in numbers:
            if number1 % 2 != 0:
                list_num2.append(number1)
    return list_num2
