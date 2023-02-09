import sys
sys.maxsize
print(sys.maxsize)   # 9223372036854775807

''
""
str()

text = 'one\ntwo\nthree'   # перенос по словам

# ------------------ Объединение
s1 = "hello" + "world"
s2 = "python"
s1+s2                   # hello world python

name = "Ivan"
age = 30
"Name:" + name +", age:" + str(age)

# ------------------- Сравнение 
s1 = '1a'
s2 = 'aa'           # y > a > A > 1
s3 = 'Aa'
s4 = 'ba'
'1a' > 'aa'  # false 
'aa' > 'Aa'  # true
'aa' > 'ba'  # false
'aa' > 'az'  # false

s1 = 'Intel' 
s2 = 'intel'
s1 == s2     # false
s1.lower() == s2.lower()  # true



