'''
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
'''

k = int(input('Введите целое число:'))
otr_f = []
f = []
result_f = []
fib_0 = 0
f.append(fib_0)
fib_1 = 1
f.append(fib_1)
fib = 0
for i in range(k):
    fib = f[i] + f[i + 1]
    f.append(fib)
    fib *= -1
    otr_f.append(fib)
# print(f)
otr_f.reverse()
# print(otr_f)
result_f = otr_f + f
print(f'Для k = {k} => {result_f}')
