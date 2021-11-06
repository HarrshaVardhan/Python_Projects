
#item is loop variable
#item variable will hold a character at a time
#for item in 'Python':
#	print(item)


for item in ['Mom','Lex','Amelia','June']:
	print(item)
	
	
for item in [1, 2, 3, 4]:
	print(item)
	
	
#Range function
for item in range(9, 20, 2): #(start, end(exclude), step)
	print(item)
	
# exercise
price = [10, 20, 30]
print(sum(price))

for data in price:
	print(sum(price))
	
	
	#Mosh solution
prices = [10, 20, 30]
total = 0
for price in prices:
	total += price
print(f"Total: {total}")
