def function(*number):
    list = []
    list.append(max(number))
    list.append(min(number))
    return list
print(function(1,2,3,4,10))


def fun(string, case=True):
    if case:
        return string.upper()
    else:
        return string.lower()
print(fun('Hello', True))


def fun(*strings, glue=':'): 
    list = []
    for string in strings: 
        if len(string) > 3: 
            list.append(string)
        
   
    return glue.join(list)
print(fun('hello','www','re','good'))
