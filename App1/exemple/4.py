# -------Вывести все элементы меньше 5-------
# [1,1,2,3,5,8,13,21,34,55,89]
list_base = [1,1,2,3,5,8,13,21,34,55,89]
#1
for c in list_base :
 if c < 5:
    print(c)
#2
print(list(filter(lambda a: a < 5,list_base)))
#3
print([s for s in list_base if s<5])   # списковое включение - наиболее предпочтительный

# ---------- Общие элементы списка 1 и 2  ------------
list_one = [1,4,3,2,66,5,93,45,22]
list_two = [3,4,22,66,1,4,9]

list_result = list_one & list_two
print(list_result)