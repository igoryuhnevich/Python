# ************************* SET{} ************************************************
# ******    Операции на множествах                                    ************
# ******    объединение , пересечение, issubset(), isdisjoint()       ************


# ------- или | объединение ----------------
lang_x = {"C++",'Perl','PHP'}
lang_y = {'Java','C#','PHP','Python'}
lang_z = lang_x.union(lang_y)         # lang_z = lang_x | lang_y
#  {'Java', 'C#', 'Python', 'PHP', 'C++', 'Perl'}

# ------- и  &  пересечение ----------------
bats_enemies = {'Darkside','Jocker','Bane'}
cups_enemies = {'General Zod','Darkside','Lode'}
JL_enemies = bats_enemies.intersection(cups_enemies)     # bats_enemise & cups_enemies
# {'Darkside'}

# --------- разность множ-в ---------------
minued = {23,44,1,34,98}
subtrahend = {23,44,1,55,76}
total = minued.difference(subtrahend)       # minued - subtrahend
# {34,98}

# --------- симметрическая разность ^ -------
f_set = {11,'a',18,'v',65,'g'}
s_set = {11,'z',32,'v',0,'g'}
t_set = f_set.symmetric_difference(s_set)   # f_set ^ s_set
# {32,0,65,18,'a','z'}

# ---------- isdisjoint() -------------------
it = {'green','white','red'}
ru = {'white','blue','red'}
ukr = {'blue','yellow'}                  # есть ли у множеств общие элементы
true_or_false = ukr.isdisjoint(it)       # true
true_or_false = ru.isdisjoint(it)        # false

# ---------- issubset() --------------------
solar_system = {'Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune'} #"I"
first_three_planet = {'Mercury','Venus','Earth'}  # проверяет, является ли "O" 
poor_small_guy = {'Pluto'}                        # подмножеством "U"
emptyness = set()                        
print(first_three_planet.issubset(solar_system))  # true   "O" <= "I"
print(poor_small_guy.issubset(solar_system))      # false  "U" <= "I"
print(emptyness.issubset(solar_system))           # true   "E" <= "I" \ "E"<="O" \ "E"<="U"
print(poor_small_guy.issubset(poor_small_guy))    # true   "U" <= "U" \ "I"<="I" \ "O"<="O"
# cтрогое подмножество < , сравниваемые наборы не должны быть идентичны
# print(poor_small_guy.issubset(poor_small_guy))    # false   "U" <= "U"
# остальные аналогичны

# ----------- issubpreset() ------------------
# надмножество 
print(solar_system.issuperset(first_three_planet))  # true  "I" >= "O"
print(poor_small_guy.issuperset(solar_system))      # false "U" >= "I"
print(poor_small_guy.issuperset(emptyness))         # true  "U" >= "E"
# строгое надмножество  > 
print(poor_small_guy > poor_small_guy)              # false 

#-----------------------------------------------------
#--------- update()--------------------
dogs_in_first_harness = {'Lessie','Bork','Spark'}
dogs_in_second_harness = {'lucky'}
dogs_in_second_harness.update(dogs_in_first_harness)   # |= {'Lessie','Bork','Spark','lucky'}
#---------inntersection_update()--------
basin_measurements_west = {-3333,4444,5555}
basin_measurements_east = {1111,-3333,2222}
basin_measurements_west.intersection_update(basin_measurements_east)   # &= {-3333}
#--------difference_update()-------------
price_may = {100,200,125}
price_june = {100,200,300}
price_may.difference(price_june)    # -=  {125}
#--------symmetric_difference_update()------
his_bag = {'croissant','tea','cookies'}
her_bag = {'tea','cookies','chocolate','waffles'}
her_bag.symmetric_difference_update(his_bag)    # ^=  {"croissant",'chocolate','waffles'}

#-------------------------------------------------------------
#----------Свойства---------------------
list_of_year = [2011,2012,2013]
set_of_year = {2001,2002,2003}
set_of_year.union(list_of_year)  # {2013,2012,2011,2001,2003,2002}
set_of_year | list_of_year       # error type(s) for |

one = set('11111')
two = set('22222')
three = set('33333')
four = set('44444')
five = set('55555')
uni_set_v1 = one.union(two,three,four,five)   # {"1","2","3","4","5"}
uni_set_v2 = one | two | three | four | five  # {"1","2","3","4","5"}

es1 = {11,21,31,311,3111}
es2 = {111,211,311,411}
es3 = {1111,2111,3111,4111}
# порядок выполнения операций слева --> направо
es1-es2-es3               # {11, 21, 31}
es1.difference(es2,es3)   # {11, 21, 31}

#--------Преобразования--------------
my_string = 'Lorem ipsum dolor sit amet'
string_to_set = {my_string}                     # {'Lorem ipsum dolor sit amet'} 
my_string1 = set('Lorem ipsum dolor sit amet')  # {'L''o''r''e''m' '' 'i'p''s'...'}

my_list = [2,4,8,16,32]
list_set_set = set(my_list)

#---------------Frozenset-----------------
ordinary_set = set()
frozen_set = frozenset()
print(ordinary_set == frozen_set)    #True
ordinary_set.add(1)
print(ordinary_set)    # {1}
frozen_set.add(1)      
print(frozen_set)      # error




