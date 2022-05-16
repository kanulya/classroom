from random import random

x = round(random()*100)
i = 1
while i <= 10:
    a = int(input(str(i) + '-я попытка: '))
    if a > x:
        print('Число меньше')
    elif a < x:
        print('Число больше')
    else:
        print('Вы угадали с %d-й попытки' % i)
        break
    i += 1
else:
    print('Вы не отгадали за 10 попыток. Было загадано', x)
