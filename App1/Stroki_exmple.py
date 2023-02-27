 # Best practices

# Разбить строку на символы
text = 'django'
# 1 
list(text)                # ['d','j','a','n','g','o']
# 2
[ c for c in "text" ]     # ['t','e','x','t']
# 3
for c in text:
    print(c)              # d
                          # j
                          # a
                          # n
                          # g
                          # o

# Из строки выделить числа
str = "h3110 23 cat 444.4 rabbit 11 2 dog"
[int(s) for s in str.split() if s.isdigit()]     # [23, 11, 2]

str = "h3110 23 cat 444.4 rabbit 11 2 dog"
import re

from macpath import split
re.findall(r'\d+',str)               # ['3110','23','444','4','11','2']

# Перевернуть строку
'test'[::-1]                # c помощью среза   str[start:end:step]

''.join(reversed('test'))   # tset 

# Удалить последний символ в строке
"Some text1" [:-1]    # c помощью среза 

# Убрать пробелы из строки
" Some text ".strip()       # "Some text"
"So m e  t e xt ".replace(' ','')   # 'Sometext'    (s,new) 

# ----stroka iterator-----
s = "python" 
it = iter(s)
print(next(it))
print(it)
print(s[2])

# Две строки. Является ли одна строка подстрокой другой.
# независимо от регистра.
def search_substr(subst,st):
    if subst.lower() in st.lower():
        return "Yes, it is"
    else:  
        return "No, is not"  
print(search_substr('FOto','Foton'))  # "Yes, it is"


# Строка и 5 операций с ней(кол-во вхождений,получение символа,все нечетные индексы
#  кол-во слов в строке)
str = 'Сидел барсук в своей норе и ел картошечку пюре'
#1
length_str = len(str)
#2
Add_str = str + '.'
#3
input_str = str.find('ре')    # "ре" in str
#4
str.count('ре')
#5
str[::-2] 
#6
str[1::2]  
#7
number_words = str.split      # str.count(' ' + 1)
len(number_words)

# Строка. Заглавная буква первая, индекс вхождения, замена, соединение
#  разбиение.
str  = 'пишите код так, как будто сопровождать его будет склонный к насилию психопат, который знает, где вы живете.'
#1
if str.islower() : str.capitalize()
#2
str.find('сопровождать')                   # str.index("сопровождать")
#3
str.replace("сопровождать","поддержать")
#4
lst = str.split(',')
','.join(lst)


# Дано имя файла. Необходимо вывести его расширение.
str = 'copley.com'                      # имя файла
#1
def extension_slice(filename):          # решается через срезы
    point_pos = filename.index('.')     # filename.find('.')    ищем индекс точки
    return filename[point_pos + 1:]     # номер позиции + точка и до конца.
#2
def extension_part(filename):
    return filename.partition('.')[2]   # возвращает картеж из трех элементов. Нам нужен третий.
                                        # ('copley', '.' ,'com')
#3 
import re
def extension_regx(filename):
    """ regex = r'\..+$'                    # экранированная точка. Ищем точку. Ищем  символы до конца строки - .+$ 
        re.search(regex,filename)[0]        # возвращает объект класса Match. Но нам нужен обект - [0], он будет с точкой. """
    regex = r'\.(.+$)'
    return re.search(regex,filename)[1]     # убираем точку.

if __name__=='__name__':
    print(extension_part(str))
    print(extension_slice(str))
    print(extension_regx(str))


# Сложите цифры целого числа
Number = 12345
#1
def sum_for(number):
    s = 0
    for item in str(number):    # перебирать строку. Каждый символ строка - '12345' (это строки)
        s = s + int(item)       # преводим в интеджер.
    return s
#2 
def sum_lst(number):
    lst = [int(item) for item in str(number)]    # прербираем элементы в строке из нешего числа иприводим 
    return sum(lst)                              # каждый элемент к int. Формируется список [1,2,3,4,5]

if __name__=='__name__':
    print("s=",sum_for(Number))
    print('s=',sum_lst(Number))

# Замените заданное число вхождения подстроки
str = '0923409238400983208'

if __name__=='__name__':
  print(str.replace('0','1',0))    # ничего не меняем           
  print(str.replace('0','1',1))    # меняем только один 0
  print(str.replace('0','1',9))    # заменяем все
  print(str.replace('0','1',10))   # заменяем все

