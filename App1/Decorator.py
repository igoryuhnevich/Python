"""
x=0


def outer():
    x=1
    def inner():
        x=2
        print('inner ', x)
    
    
    inner()
    print('outer ', x)    

outer()
print('global ', x)    


def say_name(name):
    def say_goodbay():
        print("FFFFF ffff"+ name + "ggggg")
    say_goodbay()


say_name('sergey')


def strip_string(strip_chars=' '):
    def do_strip(string):
        return string.strip(strip_chars)

    return do_strip    


strip1 = strip_string()
strip2 = strip_string("! #$:;")

print(strip1(" fdsdfsdfs ! ;"))
print(strip2(" fdsdfsdfs ! ;"))


def some_decorator(func):
    def wrapper(title):
        print ("_____________________")
        func(title)
        print ("---------------------")
    return wrapper


def some_func(title):
    print('DDDDDDDDDDDD')


some_func = some_decorator(some_func)
some_func()    
"""

import math

# Декораторы функций с параметрами

# without parametr
def func_decorator(func):
    def wrapper(x, *args, **kwargs):
        dx = 0.0001    # чем меньше , тем точнее
        res = (func(x+dx, *args,**kwargs)-func(x,*args,**kwargs))/dx
        return res
    
    return wrapper

# N1 without decor
def sin_df(x):
    return math.sin(x)    


df = sin_df(math.pi/3)
print(df)

# N2 with decorator - Производная в точке П/3
@func_decorator
def sin_df(x):
    return math.sin(x)    


df = sin_df(math.pi/3)
print(df)


# S parametramy
def df_decorator(dx = 0.01):
    def func_decorator(func):
        def wrapper(x,*args,**kwargs):
            res = (func(x+dx, *args,**kwargs)-func(x,*args,**kwargs))/dx
            return res 
        return wrapper
    return func_decorator


@df_decorator(dx=0.1)
def sin_df(x):
    return math.sin(x)


# Или так 2 --------------        # Или так 3 ---------------
#f= df_decorator(dx=0.001)        sin_df = df_decorator(dx=0.001)(sin_df)
#sin_df = f(sin_df)


df = sin_df(math.pi/3)
print(df)