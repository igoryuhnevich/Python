empty_dict ={}   # задать словарь, ассоциотивный список с ключами
empty_dict2 = dict()  # не правильно

grades = {"Grisha":80,"Tim":95}  # ключ -Grisha значение -80;
fr = grades["Grisha"]      # доступ к значению =80;

try:
 kt = grades["Kate"]            # обработка ошибок по значению
except KeyError:
 print("Оценки для Кате отсутствуют!")

gr = "Grisha" in grades   # проверка наличия ключа -true
kt = "Kate" in grades     # false

gr = grades.get ("Grisha",0)   # метод get() возвращает значение по умолчанию =80 
kt = grades.get ("Kate",0)     # 0
one= grades.get ("No One")     # None

grades["Tim"] = 99    # замена старого значения на новое
grades["Kate"] = 100  # добавляет новое значение
num = len(grades)     # длинна словаря

#****** Пример *********
tweet = {
    "user":  "grinaleks",
    "text":  "Наука о данных - потрясающая тема",
    "retweet_count": 100,
    "hashtags":["#data","#science","#datascience","#awesome","#yolo"]
}
tk = tweet.keys()     # список ключей
tv = tweet.values()   # список значений
ti = tweet.items()    # список кортежей (ключ,значение)

"user" in tk       # true использует медленное in списка
"user" in tweet    # true , то же , но бысрое in словаря
"grinaleks" in tv  # true

#****** Частота слов в тексте ******
word_count = {}   # словарь 
doc = {}          # документ
for word in doc :    #перебор слов в тексте
    if word in word_count:       #    
        word_count[word] += 1    #  если есть слово добавляет всречаемость(+1)
    else: word_count[word] = 1   #  если нет - добавляет новое слово в словарь(ключь)
# *******

from collections import defaultdict

word_count = defaultdict(int)   #  если нет ключа(слова) - добавляет значение  0. int() возвращает 0.
for word in doc:
    word_count[word] += 1       #  если есть слово добавляет всречаемость(+1)

#********************

dd_list = defaultdict(list)   # list()  возвращает пустой список
dd_list [2].append (1)     # теперь dd_list содержит(2 : [1])
dd_dict = defaultdict(dict)   # dict()  возвращает пустой словарь
dd_dict ["Grisha"]["City"] = "Seattle"  # {"Grisha" : {"City":"Seattle"}}
dd_pair = defaultdict (lambda:[0,0])
dd_pair[2][1] = 1     # теперь dd_pair содержит {2:[0,1]}
