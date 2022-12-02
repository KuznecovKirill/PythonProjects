from pyDatalog import pyDatalog 
#Посчитать сумму ряда [0, 9999999]

pyDatalog.create_terms('arrSum, N')

arrSum[N] = N + arrSum[N-1]
arrSum[0] = 1

print(arrSum[9999999]==N)
