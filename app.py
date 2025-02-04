# from calendar import firstweekday
# from codecs import namereplace_errors
# from typing import NewType
#
# print('Sarah Aladdin')
# print('*' * 10)
# price = 10
# #price is identifier
# #number is int, its the value of the identifier
# price = 20.9
# #number is floating point number
# name = 'ya mother'
# #you can also set string as a value
# print(price)
# is_published = True
# #boolean value is T or F
# #python is case sensitive
# #this program is storing simple values in comp memory
# #simp val can be numbers, str, bool
# # complex val is lists, objects
# name = 'John Smith'
# age = 20
# is_new = True
#
# #now we learn how to receive input from the user
# #parenthesis means we're calling or executing that function
# name = input('What is your name? ')
# #input means ill print and ask user for input
# #recieves input and stores it in memory using name variable
# print('Hi ' + name)
# #concatenating
# color = input('What is your favourite color? ')
# print(name + ' likes ' + color)
#
# birth_year = input('Birth year: ')
# print(type(birth_year))
# #checks if its a str bool etc
# age = 2025 - int(birth_year)
# print(age)
#
# weight_lbs = input('What is your weight in pounds? ')
# weight_kg = int(weight_lbs) / 2.2
# print(weight_kg)
#
# #now we learn more about str
#
# course = "Python's Course for Beginners"
# course2 = 'Python for "Beginners"'
# course3 = '''
# Hi John,
#
# Here is our first email to you
#
# Thank you,
# The support team
# '''
# #the different apostrophes in strings
#
# print(course[0])
# #return the first character in course
# print(course[-1])
# #we can also return a negative index, this will be the last character
# print(course[-2])
# #this will be the second last character
# print(course[0:3])
# #returns characters 0 until 2
# print(course[1:])
# #excludes the first character
# print(course[:])
# #assumes the whole string
# another = course[:]
# #clone the string into another variable
# print(another)
#
# name = 'Jennifer'
# print(name[1:-1])
#
# #now we learn about formatted strings
# #good for dynamically generating text with your variables
# first = 'John'
# last = 'Smith'
# msg = f'{first} [{last}] is a coder'
# # formatted string is prefixed with an f
# print(msg)
#
# #now we learn more abt python strings
# course = 'Python for "Beginners"'
# #len is a built in function
# #calc the number of char in this str with len
# print(len(course))
# #len enforces a character number limit for an input
# mf = 87
# print(len(str(mf)))
# #len is a general purpose function, it can also count the number of items in a list
# print(course.upper())
# #.upper turns str into uppercase
# #dot operator
# #when you type the dot, you can see all the methods
# #methods belong to objects like strings or numbers, thats the difference between a method and a function
# #method doesn't modify our original string, instead it creates a new string and returns it
# print(course.lower())
# print(course)
# #find a character or characters in a string using find method
# print(course.find('o'))
# print(course.find('Beginners'))
# #11 because B is the 11th character
# print(course.replace('Beginners', 'Absolute Beginners'))
# #method for replacing a character or characters
# print(course.replace('P', 'J'))
#
# print('Python' in course)
# #in is an operator for checking existence of a character or characters in a string
# #is a bool expression

#now we learn arithmetic operations in python
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
#division floating
print(10 // 3)
#division int
print(10 // 3)
#remainder of the divi
