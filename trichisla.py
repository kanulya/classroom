x = int(input())
y = int(input())
z = int(input())
print()
if x < y and x < z or x > y and x > z:
	print(x)
	if y < x and y < z or y > x and y > z:
		print(y)
	else:
		print(z)
elif y < x and y < z or y > x and y > z:
	print(y)
	if z < x and z < y or z > x and z > y:
		print(z)
