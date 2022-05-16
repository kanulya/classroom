n = int(input('Сколько хотите накопить? '))
s = 0
v = 0
while n > v:
    v = int(input('Взнос: '))
    s = s + v
    if s >= n:
        print('Поздравляю! Вы накопили %d сомов!'% s)
        break

