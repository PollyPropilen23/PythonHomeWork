# 2. Напишите программу, которая найдёт произведение пар чисел списка.
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import random
n = int(input('Введите количество элементов исходного списка: '))
lst = [random.randint(-10, 10) for i in range(n)]
print(lst)
result_lst = []
if n % 2 == 0:
    res_size = n//2
else:
    res_size = n//2+1
for i in range(res_size):
    pair = lst[i]*lst[-i-1]
    print(pair)
    result_lst.append(pair)
print(result_lst)
