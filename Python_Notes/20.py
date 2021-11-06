#Intro to Function
def greet_user():
	print('Hi, there!')
	print('Welcome aboard')


print('start')
greet_user()
print('finish')

#Parameter
def greet_user(name):
	#name = 'John' this function is the same as given a value to variable. don't need this.
	print(f'Hi, {name}')
	print(f'Welcome Aboard')
	

print('Start')
greet_user('Mom') #call function
print('Finish')
#print(greet_user("Mom")) # it did not return, shown None.


#Multi parameter
def greet_user(first_name, last_name):
	print(f'Hi, {first_name} {last_name}')


greet_user('Koonmei', 'Ho')#Position Argument
greet_user(last_name='Koonmei', first_name='Ho') #Keyword Argument

#Return statement
def squre(number):
	return number * number
	
#result = squre(3) 
#print(result) line 36, 37 not need to creat variblr and print
#can pass this func directly inside the print func without definding variable
#do this
print(squre(3))


#E.g

def squre(number):
	print(number * number)
	
	
print(squre(3))
	
#Output
# 9
# None <--- by default all func return to value none, represent of vlue like Null.
#The two thins need to take away by default all func in python trturn None. 
#you can change that if you have func cal something can return the result
#using return statement.



