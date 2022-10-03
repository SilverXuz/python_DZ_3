'''
Задайте список из вещественных чисел. 
Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''
spisok = [1.4, 1.69, 3.2, 5, 3.61, 10.01, 5.5]
result = 0
min = 1
max = 0

for i in range(len(spisok)):
    y = spisok[i] % 1  + 0.001
    # y = x - math.modf(x)
    # print('0', y)
    if y > max:
        max = y
    elif y == 0.001:
        print('Бог дал, бог взял')
    elif y < min:
        min = y

result = max - min
print(f'{spisok} => {result:.2f}')
