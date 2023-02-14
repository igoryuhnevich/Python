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
[int(s) for s in str.split() if s.isdigit]     # [23, 11, 2]

str = "h3110 23 cat 444.4 rabbit 11 2 dog"
import re
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


 

