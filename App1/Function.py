# Отправка письма 

def send_mail(from_name,old):
    text = f"""FFFFFFfffffFFFFI! 
    Dfdfdfdfdfd.  
    Dfdfdfdfdfdf -  {from_name } {old}."""
    print(text)


def  get_sqrt(x):
    res = None if x<0 else x** 0.5
    return x, res (x, res) # tuple


def get_max2(a,b):
    return a if a>b else b

"""
x, y, z = 5, 7, 10
print (get_max2(x, get_max2(y,z)))  # выполнится сравнение Y и Z, затем Х
"""
def get_max3(a,b,c):
    return  get_max2(a, get_max2(b,c))


x,y,z = 5,7,10
print (get_max3(x,y,z))
# *************************************************************************
def get_nod(a, b):
    """ Вычесление НОД для натуральных чисел а и в
        по алгаритму Евклида.
       :param a - первое натуральное число.
       :param b - второе натуральное число.
       :return НОД    """
    while a != b:
        if a>b:   a -=b
        else:   b -= a
    return a

res = get_nod(6,28)
print(res)
help(get_nod)


def test_nod(func):
    # test N1
    b = 28
    a = 35
    res = func(a,b)
    if res == 7: print("test1 - ok")
    else : print("test1 - not Ok")

test_nod(get_nod)
    

def cmp_str(s1, s2 ,reg=False, trim=True):
    if reg:
        s1 = s1.lower()
        s2 = s2.lower()
    if trim:
        s1 = s1.strip() 
        s2 = s2.strip()
    return s1 == s2


print(cmp_str('fff    ','Fff',True))


def add_value(value,lst=[]):   #N1 add_value(value, lst):   #N2 add_value(value, lst = None):
    lst.append(value)                                               # if lst is None:
    return lst                                                      #    lst = []

l = add_value(1)               #  l = add_value(1,[])          # l = add_value(1)       
l = add_value(2)               #  l = add_value(2,[])          # l = add_value(2)       # l = add_value(2,l)        
l = add_value(3)          
print(l)        # [1,2,3]      #  [2]                          #  [2]                   # [1,2]

l = add_value(lst = [4,5,], value = 6)
print(l)


def os_path(*args):
    print(args)


os_path('sdfsdf','wwwww','tttttt')   # на выходе КОРТЕЖ из значений аргументов. Или коллекция из значений аргументов


def os_path(*args,**kwargs):                    # def os_path(disk,*args,sep = '\',**kwargs) - disk и sep можно формально задать.
    print (kwargs)                                      # args = (disk, ) * args
                                                        # path = sep.join(args)
                                                        # if 'trim' in kwargs and kwargs['trim'] - если ключ trim есть в словаре kwargs и значение этого ключа True

p = os_path('cc','dd',sep = '/', trim = True)   # на выходе СЛОВАРЬ - {'sep':'/','trim':True}
print(p)                                        # path = kwargs['sep'].join(args)


    





