# Project exercise 
weight = float(input('Weight: '))
l_k = str(input('Is your weight in (L)bs or (K)g)? ' ))

if l_k == 'l':
	to_kg = round(weight * 0.45, 2)
	print(f'converted lbs to kg: {to_kg}')
else:
	to_lbs = round(weight * 2.2, 2)
	print(f'converted kg to lbs: {to_lbs}')


#code improvement

weight = float(input('Weight: '))
l_k = input('Is your weight in (L)bs or (K)g)? ' )

if l_k.upper() == "L": #can use string method for upper =case. 
	to_kg = round(weight * 0.45, 2)
	print(f'converted lbs to kg: {to_kg}')
else:
	to_lbs = round(weight * 2.2, 2)
	print(f'converted kg to lbs: {to_lbs}')


# Mosh solution

weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')
if unit.upper() == 'L':
	converted = weight * 0.45
	print(f'You are {converted} kilos')
else:
	converted = weight / 0.45
	print(f'You are {converted} pounds')


