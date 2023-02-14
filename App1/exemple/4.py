# -------Вывести все элементы меньше 5-------
# [1,1,2,3,5,8,13,21,34,55,89]
list_base = [1,1,2,3,5,8,13,21,34,55,89]
#1
for c in list_base :
 if c < 5:
    print(c)
#2
print(list(filter(lambda a: a < 5,list_base)))   # функция filter
#3
print([s for s in list_base if s<5])             # списковое включение - наиболее предпочтительный


# ---------- Общие элементы списка 1 и 2  ------------
list_one = [1,4,3,2,66,5,93,45,22,1]
list_two = [3,4,22,66,1,4,9,1]
#1
print(list(filter(lambda a: a in list_one,list_two)))  #функция filter         оставит все элементы - дубли
#2 
print([a for a in list_one if a in list_two])          # списковое включение     оставит все элементы - дубли
#3
print( list(set(list_one)&set(list_two)))              # привести к множеству    ( оставит по одному 
                                                       #  уникальному элементу )


# ---------- отсортировать словарь по значению (по ключу) ------
import operator

#1 по возрастанию increasing
dict_unsort = {1:2,2:4,0:0,3:2,5:3,4:6}
sort_dict = sorted(dict_unsort.items(),key = operator.itemgetter(1))  # itemgetter(0) - по ключу
print(sort_dict)                                                      # list [ ]
print(dict(sort_dict))                                                # dict(sort_dict) == dict_unsort

#2 по возрастанию decreasing
sort_dict = dict(sorted(dict_unsort.items(),key = operator.itemgetter(1),reverse=True))

#3 new
sort_dict = dict(sorted(dict_unsort.items(),key = lambda item: item[1]))


# ------------- Слияние словарей в один ---------
dict_one = {1:3,3:3,4:4,5:4}
dict_two = {6:3,12:3,11:3}
dict_three = {8:22,21:1}

#1
dict_res = {} 
for d in (dict_one,dict_two,dict_three):
    dict_res.update(d)
#2
dict_res ={**dict_one,**dict_two,**dict_three}





