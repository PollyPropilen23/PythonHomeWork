
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            # print(f'при ({x},{y},{z}) результат {(not(x or y or z)) == ((not x) and (not y) and (not z))}') #not(x or y or z) == (not x) and (not y) and (not z)
            result = ((not (x or y or z)) == ((not x) and (not y) and (not z)))
print('выражение верно для всех значений предикат' if result == 8 else 'выражение верно не для всех значений предикат')
