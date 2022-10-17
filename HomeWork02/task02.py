# 2. Напишите программу, которая принимает на вход число N и
# выдает набор произведений чисел от 1 до N.

num = int(input('Введите число N= '))
fact = 1
numbers = list()
for i in range(1, num+1):
    fact *= i
    numbers.append(fact)
print(numbers)
