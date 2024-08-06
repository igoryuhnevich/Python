#d_lipt = input("введите числа с клавиатуры -  ") 

#a = [ int(d) for d in d_lipt] 

#print(a)
# **************************************************
"""
a = [f'{i}*{j} = {i*j}'   
 for i in range(3)         # таблица умножения
 for j in range(4) ]

print(a) """
# ***************************************************
'''
matrix = [[0,1,2,3],
          [10,11,12,13],
          [20,21,22,23]]

a = [ x
        for row in matrix
        for x in row
        ]
print(a) '''


"""       # Треугольник Паскаля
N =7
P = []

for i in range(N):
    row = [1] * (i+1)
    for j in range(i):
        if j!=0 and j!=1:
           row[j] = P[i-1][j-1] + P[i-1][j]

    P.append(row)

for r in P:
    print(r)
"""
N = 5
P=[]

for i in range(N):
    row = [1] * (i+1) 
    for j in range (i+1):
        if j !=0 and j != i:
            row[j] = P[i-1][j-1] + P[i-1][j]
    P.append(row)
for r in P: 
    print(r)
