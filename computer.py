memory = int(input("Размер оперативной памяти "))
ssd = int(input("Размер жёсткого диска SSD "))
hdd = int(input("Размер жёсткого диска HDD "))
price = int(input("Стоимость "))
if memory >= 4 and memory <= 8 and ssd >= 256 or hdd >= 1000 and price<=1000:
	print("Компьютер подходит")
else:
	print("Компьютер не подойдет")
