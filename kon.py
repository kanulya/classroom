kx = int(input("Координаты коня по горизонтали "))
ky = int(input("Координаты коня по вертикали "))
fx = int(input("Координаты фигуры по горизонтали "))
fy = int(input("Координаты фигуры по вертикали "))
a = abs(kx-fx)
b = abs(ky-fy)
if a == 1 and b == 2 or a == 2 and b == 1:
    print('Конь бьет фигуру')

else:
    print('Не бьет(')
