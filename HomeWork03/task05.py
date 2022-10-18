# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

k = int(input('введите чсло '))
fib = [0, 1]
for i in range(2, k+1):
    n = fib[i-1]+fib[i-2]
    fib.append(n)
for i in range(-k, 0):
    n = int((-1)**(i)*fib[i])  # не i+1, тк нумерация элементов списка с 0
    fib.insert(0, n)
print(fib)
