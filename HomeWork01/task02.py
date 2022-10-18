# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.
#result = 0
result = list()
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            # print(f'при ({x},{y},{z}) результат {(not(x or y or z)) == ((not x) and (not y) and (not z))}') #not(x or y or z) == (not x) and (not y) and (not z)
            #result = result + ((not (x or y or z)) == ((not x) and (not y) and (not z)))
            res = ((not (x or y or z)) == ((not x) and (not y) and (not z)))
            result.append(res)
print('выражение верно для всех значений предикат' if all(result) else 'выражение верно не для всех значений предикат')
