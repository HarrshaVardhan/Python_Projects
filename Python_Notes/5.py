#This is particulary useful when we recieved input from the user. When we filled out thr form online. Each input fills always have a limit. we can force the limit the number of characters in input fills.

#in the future when we look at list, we can use this function to count the number of the itmes in the list.

#its general purpose function

course = 'Python for Beginners'
print(len(course)), print(course)
#print, len are general purpose in function they don't belong to any type data

print(course.upper(), end=' '), print(course.lower())
#course.upper() refer to this function as method, specific to string.

print(course.find('P'), end=' '), print(course.find('o'))
#want to find a char, a sequance use find method, index of the occurance.

print(course.find('O'))
#don't have Upper case 'O' anywhere in this string #output -1

print(course.find('Beginners'))
#can pass a sequance of characters the words beginner start from index 11

print(course.replace('Beginners', 'Absolute Beginners'))
print(course.replace('P', 'J'))
#replace

print('Python' in course) 
#boolean value
#find method words

