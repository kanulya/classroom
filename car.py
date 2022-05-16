b = input("Car brand: ")
t = "toyota"
l = "lexus"
m = int(input("Mileage: "))
c = input("Color: ")
w = "white"
g = "grey"
h = input("Which hand drive car: ")
lt = "left"
o = int(input("Owners quantity: "))
p = int(input("Price: "))
if b == t or b == l and c == w or c == g and h == lt and o <= 2:
	if m <= 150000 and p <= 10000 and o <= 2:
		print ("Lets look this car")
	elif m <= 200000 and p <= 8000 and o <= 2:
		print("Lets look this car.")
else:
	print("Lets look another car. ")
