# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

num = int(input('введите номер четверти: '))
if num==1:
    print('x>0, y>0')
elif num==2:
    print('x<0,y>0')
elif num==3:
    print('x<0,y<0')
elif num==4:
    print('x>0,y<0')
else:
    print('такого номера четверти не существует')
