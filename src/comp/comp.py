# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = [h.name for h in humans if h.name.startswith("D")]
print(a)

print("\n ----------------------")
# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = [e.name for e in humans if e.name.endswith("e")]
print(b)

print("\n ----------------------")

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
C_G = list("CDEFG") # only names that start with these letters
c = [c.name for c in humans if c.name[0] in C_G] # This was took some time
print(c)

print("\n ----------------------")

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = [i.age + 10 for i in humans] 
print(d)

print("\n ----------------------")

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = ["{}-{}".format(i.name, i.age) for i in humans]
print(e)

print("\n ----------------------")

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
A_range = list(range(27, 33))  
f = [(i.name, i.age) for i in humans  if i.age in A_range]
print(f)

print("\n ----------------------")

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names uppercase:")
# g = [(i.age + 5, i.name.upper()) for i in humans] # For some reason the test did not like this.

from copy import deepcopy
def new_H(i): # param 
    i.age = i.age + 5
    i.name = i.name.upper()

    return i 

g = [new_H(deepcopy(i)) for i in humans]

print(g)

print("\n ----------------------")

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = [math.sqrt(i.age) for i in humans]
print(h)
