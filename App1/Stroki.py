import sys       # Python 3 - utf 8

""" 
1.Кодировка строк
2.Максимальная длина строки в Python
3.Пустая строка Python
4.Перенос строк
5.Конкатенация строк
6.Сравнение строк
7.Как удалить строку в Python
8.Обращение по индексу
9.Форматирование %, f-str, Template Str, format
 """

sys.maxsize
print(sys.maxsize)   # 9223372036854775807

# ------------------- Пустая строка
''
""
str()

# ------------------- Перенос по словам
text = 'one\ntwo\nthree'  

# ------------------ Объединение
s1 = "hello" + "world"
s2 = "python"
s1+s2                   # hello world python

name = "Ivan"
age = 30
"Name:" + name +", age:" + str(age)

# ------------------- Сравнение 
s1 = '1a'
s2 = 'aa'           # y > a > A > 1
s3 = 'Aa'
s4 = 'ba'
'1a' > 'aa'  # false 
'aa' > 'Aa'  # true
'aa' > 'ba'  # false
'aa' > 'az'  # false

s1 = 'Intel' 
s2 = 'intel'
s1 == s2     # false
s1.lower() == s2.lower()  # true

#------------------- Удаление строк
s = 'test'
s.replace('test','')    # ' '

s = 'test'
s = ''
s                      # ' '

# ----------------- Индекс 
s ='abcdef'
s[0]  # a
s[1]  # b
s[2]  # c
s[-1] # f

# --------------- Форматирование
# %
name = 'Alex'
'Hello, %s' % name       # "Hello, Alex"
# %d %s %c %r 
'%d %s, %d %s' %(6,'bananas',10,'lemons')   # "6 bananas , 10 lemons"

# str.format()
'{}'.format(100)        # 100
'{0},{1},{2}'.format('one','two','three')     # 'one, two, three'
'{2},{1},{0}'.format('one','two','three')     # 'three, two, one'

# f-строка    самая популярная
name = 'Alex'
f'Hello,{name}!'       # 'Hello,Alex!'

a = 5
b = 10
f'Five pluse ten is {a+b} and not {2*(a+b)}'

# Template Strings
from string import Template
name = 'Alex'
age = 30
s = Template('My name is $name. Im $age')
print(s.substitute(name=name,age=age))



 










