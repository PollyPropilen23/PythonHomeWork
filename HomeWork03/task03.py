# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
#  между максимальным и минимальным значением дробной части элементов.
from decimal import Decimal

lst = list(map(str, input('введите вещественные числа через пробел: ').split()))
print(lst)
res_lst = []
for i in lst:
    n = abs(Decimal(i) % 1)
    res_lst.append(n)
print(max(res_lst)-min(res_lst))
