l = input("Язык программирования: ")
a = int(input("Возраст: "))
o = int(input("Опыт работы: "))
z = int(input("Желаемая зарплата: "))
x = "python"
y = "java"
j = "javascript"
if l == x or l == y or l == j and a >= 18 and a < 65 and o >= 3 and z < 60000:
	print('Вы нам подходите')
else:
	print('Вы нам не подходите')
