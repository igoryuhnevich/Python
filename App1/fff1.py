# Рекурсивная функция : 
#    результат 1,2,3,4,4,3,2,1

def recursive(value):
    print(value)
    if value < 4:
        recursive(value+1)
    print(value)
recursive(1)        


def fact(n):
    if n <= 0:
        return 1
    else:
        return n*fact(n-1) 


# lambda func

lst = [5,3,0,-6,8,10,1]


def get_filter(a,filter = None):
    if filter is None:
        return a

    res =[]        
    for x in a:
        if filter(x):
            res.append(x)

    return res


e = get_filter(lst)                        # без фильтра
r = get_filter(lst, lambda x : x % 2 == 0) # фильтр - проверка на четность    
t = get_filter(lst, lambda x : x > 0)      # для четных значений  


