s = some_function_that_returns_a_string()  #возвращает строковое значение
if s:
    first_char = s[0]     # первый символ в строке
else :
    first_char =''

# *************

first_char = s and s[0]  # возвращает второе значение, если первое истина;
                         # первое значение, в случае если оно ложно

safe x = x or 0      # если х является либо числом, либо,возможно, None,
                     # то результат будет числом

# ***  Встроенные функции Python ***********

all([True,1,{3}])    # True
all([True,1,{}])      # False , {} - ложное
any ([True,1,{}])    # True, True - истина
all([])              # True, нет ложных элементов
any([])              # False,нет истинных элементов
