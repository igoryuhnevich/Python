s = set ()  # задать пустое множество
s.add (1)   # s = {1}
s.add (2)   # s = {1,2}
s.add (2)   # s = {1,2}
x = len (s) # = 2
y = 2 in s  # true
z = 3 in s  # false
# поиск in в множествах очень быстрый

#проверка на пренадлежность некоторой последовательности
stopw_list = ['a','an','at'] + 'other_words' + ['yet','you']
'zip' in stopw_list     # false, проверяется каждый элемент
# множество стоп-слов
stopw_set = set(stopw_list)
'zip' in stopw_set      # очень быстрая проверка

#получение уникальных элементов в наборе данных
item_list = [1,2,3,1,2,3] 
num_items = len( item_list) # =6
item_set = set(item_list)   # вернет множество {1,2,3}
num_ditems = len(item_set)  # число недублирующихся = 3
dis_item_list = list(item_set)  # назад в список = [1,2,3]


