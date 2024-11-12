# Booleans in python 
# Boolean Values
True
False
a = 10
b = 20
if a < b :
    print(True)

print("*" * 20)

c = 17
d = 18

if d >= 18 :
    print(True)
    print("Eligible to drive")
else:
    print(False)
    print("Not Eligible to drive")

# or

print("*" * 20)
print(10>9)
print(10 == 9)
print(10 < 9)

# evaluate values and variables 
print("*" * 20)
print(bool("RadhaKrishna"))
print(bool(15))

# or

print("*" * 20)
e = "RadhaKrishna"
f = 30
print(bool(e))
print(bool(f))

# &
# false values

print("*" * 20)
g = ''
h = 0
print(bool(g))
print(bool(h))

# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.

# filled > will display true 
print("*" * 20)
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))

print("*" * 20)
# empty > will display false  
print(bool(None))
print(bool(False))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# One more value, or object in this case, evaluates to False, and that is if you have an 
# object that is made from a class with a __len__ function that returns 0 or False:

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

# functions can return a boolean
def myFunction() :
  return True

print(myFunction()) 

# You can execute code based on the Boolean answer of a function:

# Example
# Print "YES!" if the function returns True, otherwise print "NO!":

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

# Python also has many built-in functions that return a boolean value, like the isinstance() function,
#  which can be used to determine if an object is of a certain data type:
# Example
# Check if an object is an integer or not:

x = 200
print(isinstance(x, int))
