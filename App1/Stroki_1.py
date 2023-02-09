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




