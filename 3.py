#Здесь проводились пробы применение лямбда функции.

from math import sqrt
lis = [[1, 2], [3, 4]]
f = lambda x: sqrt(x[0]*x[1])
print(list(map(f, lis)))
