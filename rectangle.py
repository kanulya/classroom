# Построить
# класс для описания плоской геометрической фигуры: Rectangle (Прямоугольник.). 
# Класс
# должен содержать:
# Данные:
# длина и ширина прямоугольника 
# Методы для операций с данными: 
# Нахождения периметра, площади, изменения размеров, печати результата.
# Написать
# программу, демонстрирующую работу с этим классом. Программа должна содержать
# меню, позволяющее осуществить проверку всех методов класса.


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def square(self):
        return self.a * self.b
    def perimeter(self):
        return (self.a + self.b) * 2
    def change(self, newa, newb):
        self.a = newa
        self.b = newb
    def vyvod(self):
        print(f'Периметр треугольника = {self.perimeter()}, Площадь треугольника = {self.square()}')
rec = Rectangle(3, 5)
while True:
    print("1 = vyvod \n 2 = izmeneniya")
    a = int(input())
    if a == 1:
        rec.vyvod()
    elif a == 2:
        newa = int(input())
        newb = int(input())
        rec.change(newb=newb, newa=newa)
    else:
        print('Error')
