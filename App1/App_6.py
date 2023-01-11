import random
import sys
import time
import re
from collections import defaultdict , Counter

arr = [random.randint(0,50) for i in range(10)]
print(arr)

my_regist=re.compile("[0-9]+",re.I)

lookup = defaultdict(int)
my_counter = Counter()

def double(x) :
 return x*2 

def my_print(message="Hello, Python") :
    print(message)
my_print("Hi, igor")
my_print(123)
print(2)

def subtract(a=0,b=0):
    return a-b
subtract(10,5) # 5
subtract(0,5)  #-5
subtract(b=5)  #-5

tab_string='\t'         #обозначает символ \t
not_tab_string=r"\t"    #обозначает символы \ и t
print(len(tab_string))

try:
    print(0/0)
except ZeroDivisionError :
    print("нельзя делить на ноль")