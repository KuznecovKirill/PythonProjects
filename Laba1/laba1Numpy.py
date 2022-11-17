import numpy as np
import random
a = np.arange(0.0,9999999.0)
print("Сумма ряда",np.sum(a))
print("Среднее значение",np.mean(a))
b = np.random.randint(0,100,10000)
print("Сумма ряда случайных чисел",np.sum(b))