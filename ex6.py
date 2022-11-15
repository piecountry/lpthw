#this is a variable setting the number of types of people
types_of_people = 10

#this variable saves a string
x = f"There are {types_of_people} types of people."

#this variable saves a string
binary = "binary"

#this variable saves a string
do_not = "don't"

#this variable saves a string
y = f"Those who know {binary} and those who {do_not}."

#this function prints a string in a variable
print(x)

#this function prints a string in a variable
print(y)

#this function prints a formatted string literal
print(f"I said: {x}")
#this function prints a formatted string literal
print(f"I also said: '{y}'")

#this variable stores a boolean value (True, or False)
hilarious = False

#this variable saves an unformatted string
joke_evaluation = "Isn't that joke so funny?! {}"

#this function prints an unformatted string with the formatted string value of a boolean
print(joke_evaluation.format(hilarious))

#this variable saves an unformatted string
w = "This is the left side of..."

#this variable saves an unformatted string
e = "a string with a right side."

#this function concatenates 2 strings and prints them on the same line
print(w + e)
