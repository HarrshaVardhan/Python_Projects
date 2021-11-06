#if temperature is greater than 30
#	it's a hot day'
#otherwise if it's less than 10'
#	it's a cold day'
#otherwise
#	it's neither hot nor cold

temperature = 31

if temperature > 30: #boolean operations !=, == 
	print("It's a hot day")
else:
	print("It's not a hot day")
	
	
	#exercise
#if name less than 3 characters long
#	name must be at least 3 characters
#otherwise if it's more than 50 characters long.'
#	name can be a maximum of 50 characters
#otherwise
#	name looks good!


name = int(len(input('Pls fill your name: ')))

if name < 3:
	print('name must be at least 3 characters')
elif name >= 20:
	print('name must be maximum 20 characters')
else:
	print("name looks good!")
	
	
#Mosh solution

char_name = 'Llll'

if len(char_name) < 3:
	print('Name must be at least 3 characters')
elif len(char_name) > 50:
	print('name must be maximum 50 characters')
else:
	print('Name looks good!')

