# Numbers in python 
int 
float
complex

a = 1
print(type(a))
print(a)

b = 4.5
print(type(b))
print(b)

c = 2 + 5j
print(type(c))
print(c)


# integer 
d = 356488999222
print(type(d))
print(d)

e = -52633466
print(type(e))
print(e)

# float 

f = -35.59
print(type(f))
print(f)

g = 35e3
print(type(g))
print(g)

h = -87.7e100
print(type(h))
print(h)

i = 9E4
print(type(i))
print(i)

# In Python (and many other programming languages), 
# the letter E in a number like 12E4 is shorthand for scientific notation,
# representing "times ten raised to the power of". So, 12E4 means: 12×10 raised 4 = 120000
# 10 raised 4 =10×10×10×10=10000 | 12×10000=120000
# No,
# there is no difference in meaning between uppercase E and lowercase 
# e in scientific notation in Python.
# Both represent "times ten raised to the power of."

# complex
j = 3 + 5j
print(type(j))
print(j)

k = -5j
print(type(k))
print(k)

# type conversion 
l = 1 # still its an integer value
m = complex(l) # now its converted in complex value 
print(type(m)) #successfully converted.

n = 4.5 
o = int(n)
print(type(o))
print (o)

# Random Number 
# print('*' * 10)
# import random 
# print(random.randrange(1,10))

import random

# Generate a random float
random_float = random.random()

# Generate a random integer between 1 and 10
random_int = random.randint(1, 10)

# Shuffle a list
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)


