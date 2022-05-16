dom = input("Район местонахождения дома: ")
x = "чон арык"
y = "байтик"
z = "ортосай"
dm = input("Дом из кирпича или пескоблока? ")
k = "кирпич"
p = "пескоблок"
u = int(input("Размер участка: "))
price = int(input("Стоимость: " ))
if dom == x or dom == y or dom == z:
	if dm == k and u <= 4 and price <= 50000:
		print("Мы рассмотрим ваш дом.")
	elif dm == p and u <= 5 and price <= 45000:
		print("Мы рассмотрим ваш дом.")
else: 
	print("Ваш дом нам не подходит.")
