#!/usr/bin/env python3

print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
# bug: missing height = input()
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

# bug: missing from sys import argv
from sys import argv
script, filename = argv
# bug: txt = open(filenme)
txt = open(filename)

# bug: print("Here's your file {filename}:")
print(f"Here's your file {filename}:")
# bug: print(tx.read())
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)
# bug: print(txt_again_read())
print(txt_again.read())

# bug: print('Let's practice everything.')
print('Let\'s practice everything.')
# bug: print('You\'d need to know \'bout escapes <br> with \\ that do \n newlines and \t tabs.')
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

# bug: print("--------------)
print("--------------")
print(poem)
# bug: print(--------------)
print("--------------")

# bug: five = 10 - 2 + 3 -
five = 10 - 2 + 3 - 6
# bug: print(f"This should be five: {five}"
print(f"This should be five: {five}")

# bug: def secret_formula(started)
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    # bug: crates = jars  100
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
# bug: beans, jars = secret_formula(start_point)
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
# bug: formula = secret_formula(startpoint)
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))

people = 20
# bug: cates = 30
cats = 30
dogs = 15


if people < cats:
    # bug: print "Too many cats! The world is doomed!"
    print("Too many cats! The world is doomed!")

if people < cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

# bug: if people > dogs
if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

# bug: if people <= dogs
if people <= dogs:
    # bug: print("People are less than or equal to dogs.)
    print("People are less than or equal to dogs.")

#bug: if people = dogs:
if people == dogs:
    print("People are dogs.")
