# 5. Реализуйте алгоритм перемешивания списка.
import random
my_list = list(input('Задайте элементы списка через пробел ').split())
print(my_list)
random.shuffle(my_list)
print(my_list)
