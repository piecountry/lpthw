#!/usr/bin/env python3

from sys import argv
script, threshold = argv

def while_test(stop):
    i = 0
    numbers = []
    stop = int(stop)

    while i < stop:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += 1 # If you try i += i instead, you will get an infinite loop. Don't do it.
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    return numbers

numbers = while_test(threshold)

print(f"The size of the returned list is {len(numbers)} items.")

print("The numbers: ")

for num in numbers:
    print(num)
