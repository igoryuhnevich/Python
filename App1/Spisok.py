integer_list=[1,2,3]                               # list of numbers
heterogeneous_list=["строка",0.1,True]             # разнородный список  
list_of_lists=[integer_list,heterogeneous_list,[]] # список списков

list_length=len(integer_list)  # длина списка =3
list_sum=sum(integer_list)     #сумма значений в списке =6

""" Доступ к списку , значение ... """

x=list(range(10))  # задает список (0.1.2.3...9)
zero=x[0]    # индекс первого элемента 0
one =x[1]    # индекс второго элемента 1
eight=x[-2]  # индекс предпоследнего элемента 8
nine =x[-1]  # индекс последнего элемента 9
x[0] = -1    # присвоение [0] [-1]  теперь (-1,1,2,3...9)

""" Нарезка элементов """

first_three= x[:3]      # первые три = (-1,1,3)
three_to_end= x[3:]     # с третьего до конца (3,4,5...9)
one_to_four= x[1:5]     # (1,2,3,4)
last_three= x[-3:]      # (7,8,9)
without_first_and_last=x[1:-1]  # без первого и последнего (1,2...8)
copy_of_x= x[:]         # копия списка

""" 1 ln [1,2,3]  # True
    0 ln [1,2,3]  # False
""" 

"""  Сложение списков """

x = [1,2,3]
x.extend([4,5,6])   # (1,2,3,4,5,6)
y = x +[4,5,6]      # х без изменения

x.append(0)   # теперь х=(1,2,3,0)
y= x[-1]      # 0
z= len (x)    # 4

""" Распоковка """

x,y = [1,2]   # x=1 y=2
_,y = [1,2]   # y=2
 

