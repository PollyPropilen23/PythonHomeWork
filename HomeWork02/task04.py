# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

import random

n = int(input('Введите число N= '))
nums = list()
for i in range(n):
    i = random.randint(-n, n)
    nums.append(i)
print(nums)
res = 1
count = 0
with open('file.txt', 'r') as file:
    for line in file:
        if int(line) <= len(nums):
            # print(int(line)) для проверки
            res *= nums[int(line)-1]
            count += 1
print('нет совпадений' if count == 0 else res)
