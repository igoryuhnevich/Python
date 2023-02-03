# ************************ SET{} *******************************************************************

some_dict = {'key_one': 'val_one', 'key_two': 'val_two'}
some_set = set(some_dict)
print(some_set)
print(some_dict)

""" 
some_list = {['Great cake','hhhh','kkkk']}                     |
print(some_list)                                               |
some_dict = {{'key_one': 'val_one', 'key_two': 'val_two'}}     |__erorr dict / list__
 print(some_dict)                                              |                         
"""

card_suit = ['heart','diamand','club','spade','spade']
suit_set = set(card_suit)
print(suit_set)
print(card_suit)

""" tricky_list = [{'jocker': 'black'}, {'jocker': 'red'}]     __eroor dict__
sad_set = set(tricky_list)
print(sad_set) """

s = {1,2,3,4,5,6,6}
print(s)
print(type(s))

list = [1,2,3,4,5]
s_1 = set(list)
print(s_1)

empty_set = set()    # empty set()
print(empty_set)

another_empty_set = {}    # empty dict
print(another_empty_set)  

maybe_empty_set  = {''}   # set {''}
print(maybe_empty_set)
print(len(maybe_empty_set))
print(type(maybe_empty_set))
print(bool(maybe_empty_set))
print(bool(another_empty_set))

# ----- два множ-ва. пересечения ------------
unbreakable_diamand = ['jotaro','josuke','koichi']
golden_wind = ['jotaro','koichi','giorno']
overlap = set(unbreakable_diamand) & set(golden_wind)   
print(overlap)

# ------ добавление элемента ----------------
status = {1.22,3.44,5.0}
status.add(14.5)
print(status)

# -------удаление элемента ------------------
ыуе_цшер_удуьутеы = {'я элемент',"я тоже"}
print(ыуе_цшер_удуьутеы)
ыуе_цшер_удуьутеы.clear()   # очистить множ-во
print(ыуе_цшер_удуьутеы)
# remove
point_coord = {('x',54.4),('y',34.4),('z',22.5)}
print(point_coord)
point_coord.remove(('x',54.4))   
# dicard
point_coord.discard(('z',34.4))  # ничего не произойдет, remove() вызовет try/catche.
# pop
sweet = {'candy','gingerbread','lollipop','canddy floss','sweets'}
sweet.pop()     # удалит один рандомный элемент
print(sweet)

# ---------- перебор элементов -----------------
itarate_me = {1.1,1.2,1.3,1.4,1.5}
for num in itarate_me:
    print(num)

berry_club = {'Tomato','Currant','Sea buckthorn','Grape','Barberry'}
True_or_false = 'Tomato'in berry_club    # true
True_or_false = 'Potato' in berry_club   # false

# -----------сортировка---------------------
some_digits = {1,33,4,56,22,56,21,-12}
sort_digits = sorted(some_digits)        # [-12,1,4,21,22,33,56]
cities = {'Москва', 'Калининград', 'Новосибирск', 'Архангельск', 'Белгород', 'Хабаровск'}
sort_cities = sorted(cities)             # [Архангельск,Белгород,Калининград,....]
