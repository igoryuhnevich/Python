my_tuple= (1,2)
other_tuple = 3,4 

try:
    my_tuple[1] =3
except TypeError:
    print("кортеж изменять нельзя")


"""   Функуции и кортежи """

def sum_and_product (x,y) :
    return (x+y) , (x*y)
sp = sum_and_product(2,3)    # =(5 , 6)
s,p = sum_and_product(5,10)  # s = 15, p = 50

x,y =1,2 
x,y= y, x    # x=2 y=1

