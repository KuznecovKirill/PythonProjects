from pyDatalog import pyDatalog 
#Посчитать сумму ряда 

pyDatalog.create_terms('arrSum, N, AVS')

arrSum[N] = N + arrSum[N-1]
arrSum[0] = 1

print(arrSum[200]==N)

# Среднее значение ряда
AVS[N] = (N + 1)/2
print(AVS[200]==N)
