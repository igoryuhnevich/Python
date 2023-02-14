""" 
1.Функции для работы со строками
2.Методы для работы со строками
3.Преобразование из строки в другой тип
4.string → int
5.string → list
6.string → bytes
7.string → datetime
8.string → float
9.string → dict
10.string → json
 """
n = 10 
s = "stroka"
str(n)  # преобразование к строке
len(s)  # длина строки
chr(s)  # получение символа по ASCII
ord(s)  # получение ASCII по символу


# Возвращает индекс первого вхождения подстроки в S или -1 при отсутствии. 
# start - end .    find (s,start,end)
text = "Wikipedia is a Python library that makes it easy to access and parse data from Wikipedia"
text.find("Wikipedia")     # 0
#  rfind (s,start,end)  возвращает индекс последнего вхождения
text.rfind("Wikipedia")    # 79
#  replace(s,new)     меняет последовательность s на новую подстроку new
text.replace("from Wikipedia", "from https://www.wikipedia.org/")
'Wikipedia is a Python library that makes it easy to access and parse data from https://www.wikipedia.org/'
#  split(x)       разбивает строку на подстроки, делитель х
text.split('')            # ['Wikipedia', 'is', 'a', 'Python', 'library', 'that', 'makes', 'it', 'easy', 'to', 'access', 'and', 'parse', 'data', 'from', 'Wikipedia']
split_text = text.split('')
#  join(x)        соединяет строки в одну , делитель х
'_'.join(split_text)      # 'Wikipedia_is_a_Python_library_that_makes_it_easy_to_access_and_parse_data_from_Wikipedia'
#  strip(s)       убирает пробелы с обеих сторон
text = '   test '
text.strip()     # 'test'
#  lstrip(s), rstrip(s)  убирает пробелы только слева или справа
text.lstrip()    # 'test '
text.rstrip()    # ' test'
#  lower()/upper()       перевод всех символов в нижний/верхний регистр
text = "Python is a product of the Python Software Foundation"
text.lower()         # 'python is a product of the python software foundation'
text.upper()         # 'PYTHON IS A PRODUCT OF THE PYTHON SOFTWARE FOUNDATION'
# capitalize()           первая буква в верхний регистр, остальные в нижний 
text = "python is a product of the python software foundation"
text.capitalize()    # 'Python is a product of the python software foundation'


# Преобразование строки в другой тип
# int
int('10')                # 10
int('0x12F',base=16)     # 303
# list
'one two three four'.split()          # ["one","two","three","four"]
'one, two, three, four'.split(',')    # ["one","two","three","four"]  
# bytes
'Bytes'.encode('utf-8')       # '\xd0\x91\xd0\xb0\xb9\xd1\x82\xd1\x8b'
# datetime
from datetime import datetime
datetime.strptime('jan 1 2020  1^33PM',"%b %d %Y %I :%M%p")  # 2020-01-01  13:33:00
# float
float('1.5')    # 1.5
# dict
import json
json.loads('{"Russia":"Moscow", "France":"Paris"}')     # {"Russia":"Moscow", "France":"Paris"}      
# json
import json
json.dumps("hello")   # ' "hello" '



























