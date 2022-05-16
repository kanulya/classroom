
a = 0
s = 0
while a <= s:
    print(a)
    a += 1
    s += a
    if s > 1000:
        break
print(s)

a = 0
while a <= 100:
    a = int(input())
    if a > 100:
        print('Вы ввели число больше 100')
        break
