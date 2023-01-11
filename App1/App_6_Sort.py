import random
import sys
import time
import re
from collections import defaultdict , Counter

arr = [random.randint(0,50) for i in range(10)]
print(arr)
my_regist=re.compile("[0-9]+",re.I)
print(my_regist)
lookup = defaultdict(int)
my_counter = Counter()
print(my_counter)