#Quotes inside the quotes
course = 'Python for "Beginners"'
print(course)


#multiple line quote
course_two = ''' 
Hi, John,

Here is our first email to you.

Thank you,
The support team


'''
print(course_two)


#index each string
some_text = ("Lucian")

print(some_text[0]) #one char frome the left.
print(some_text[-1]) #one char count from the right.
print(some_text[-6])
print(some_text[:3]) #first three char from left 0-2 excluded third char

print('-' * 10)

print(some_text[0:]) #start from first char selected from left to right.
print(some_text[1:]) #show the from the right, exclude the 0 char shown from 1 to end.
print(some_text[:5]) #exclude the 5 char only show from 0 - 4.
print(some_text[:3]) #exclude the right show only the left.

print("-" * 10)

#index can clone
py = ('Python')
another = py[:]
print(another)


#exercise
name = 'Jenifer'
print(name[1:-1])
#output
# enife
