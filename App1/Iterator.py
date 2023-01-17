import sys
from itertools import repeat 

b = [1,3,5,7,9]    # spisok
iter(b)
it = iter(b)
print(it)
print(next(it))
next(it)
print(it)

s = "python"  #  stroka
it = iter(s)
print(next(it))
print(it)
print(s[2])

r=range(5)   #  function
print(r)
it = iter(r)
next(it)
print(it)
print(next(it))

for x in [1,2,3,4,5]:   # for 
 print(x)
for x in "python":
    print(x)
for x in range(5):
    print(x)    

f = repeat(4, times = 1_000_000)   # итератор представляет 4 млн. четверок. Итератор вместо списка
print(sys.getsizeof(f))            # весит 48Кб      экономно  

f = [4] * 1_000_000                # список 4 млн. 
print(sys.getsizeof(f))            # весит 76Мб      неэкономно + много времени 







