def recurPower(base, exp):
	
	if exp == 0:
		return 1
		
	else: 
		return base * recurPower(base, exp - 1)

a = recurPower(2, 9)

print a