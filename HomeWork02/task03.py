# 3. Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.


n = int(input('Введите число N= '))
numbers = list()
sum = 0
for i in range(1, n+1):
    num = (1+1/i)**i
    numbers.append(num)
    sum += num
    i += 1
print(numbers)
print(sum)
