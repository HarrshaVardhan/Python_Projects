birth_year = input('Birth year: ')
print(type(birth_year))
age = 2021 - int(birth_year)
print(type(age))
print(age)
#input is string wheather number


#exercise
#Ask a user their weight (in pounds), conver it to kilograms and print on terminal.

print('converting in pounds to kilograms')
kilogram = 0.453592
weight_pounds = input('What is your weight in pounds ')
converted = round(int(weight_pounds) * kilogram, 2)
print('p to kg is ', converted)


#Mosh solution
weight_lbs = input('Weight (lbs): ')
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)
