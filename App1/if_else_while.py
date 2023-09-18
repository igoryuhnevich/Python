if 1>2:
 message = "если 1 была больше 2..."
elif 1>3:
  message = "elif означает - else if"
else:
   message = "когда все предыдущие условия не выполняются, используется else"

# *******
""" parity = "четное" if x % 2 == 0 else "нечетное" """

# *******
x = 0
while x < 10 :
    print (x,"меньше 10")
    x += 1 

# *********
for x in range (10):
    print(x,"меньше 10")
    x += 1

# *********
for x in range(10) :
    if x == 3:
        continue   # перейти к следующей итерации
    if x == 5:
        break
    print (x)     # выйти из цикла    0 1 2 4 

# --------------------------------
# функция получает список из целых чисел. 
# Результат- новый список, в котором содержатся только те числа, которые больше 5 по модулю.
def more_then_five(lst):
    new_lst = []
    for num in lst:
        if abs(num) > 5 :
            new_lst.append(num)
    return new_lst     

print(more_then_five([-11,2,3,55,-23,535,0]))

#---------------------------------
# Cтрока из букв разных регистров. Очистить от заглавных литер.
letters = 'KJdjdjKKdjdjdcioeLLmMMM'
clear_str = ''
for letter in letters:
    if  letter.islower():
        clear_str += letter
print(clear_str)
print(letters)

# ---------------------------------
# Таблица из алфавита 33 знаков
rus_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
for pos in range(11):
    print('^'*27)
    for letter in rus_lower:
        if rus_lower.index(letter) % 11 == pos:
            print('| ',letter.upper(),letter,' |', end='')
    print()
print('^'*27)

# -----------------------------------
# Запрос имя пользователя из списка. Ввод с клавиатуры.
nick = input() 
secret_list = ['RRR','TTT','EEE','WWW']

while nick not in secret_list:
    print('Not in list')
    nick = input()
else : print (f'You are greate! {nick}')
 

    