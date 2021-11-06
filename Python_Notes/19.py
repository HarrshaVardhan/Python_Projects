names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
names[0] = 'Jon'
print(names[2:])
print(names)

#exercise

numbers = [1, 2, 3, 4, 100]
print(max(numbers))

max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)


