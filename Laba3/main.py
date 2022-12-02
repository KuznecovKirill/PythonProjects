from pyDatalog import pyDatalog 
import random
#Посчитать сумму ряда 

pyDatalog.create_terms('arrSum, N, AVS, arrRandom')

arrSum[N] = N + arrSum[N-1]
arrSum[0] = 1

print(arrSum[200]==N)

# Среднее значение ряда
AVS[N] = (N + 1)/2
print(AVS[200]==N)

# Сумма ряда случайных чисел [1,100]
arrRandom[N] = random.randint(0,100) + arrRandom[N - 1]
arrRandom[1] = random.randint(0, 100)
print(arrRandom[100]==N)
