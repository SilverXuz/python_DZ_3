'''
Напишите программу, которая найдёт произведение пар чисел списка. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
'''

import random

n = int(input('Введите размер списка:'))
spisok = []
mult_spisok = []

for i in range(n):
    spisok.append(random.randint(0,10))

for i in range(n // 2):
    x = spisok[i] * spisok[- i - 1]
    mult_spisok.append(x)
if n % 2 != 0:
    mult_spisok.append(spisok[n // 2] ** 2)
print(f'{spisok} => {mult_spisok}')
