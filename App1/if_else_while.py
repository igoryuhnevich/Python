if 1>2:
 message = "если 1 была больше 2..."
elif 1>3:
  message = "elif означает - else if"
else:
   message = "когда все предыдущие условия не выполняются, используется else"

# *******
parity = "четное" if x % 2 == 0 else "нечетное"

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





