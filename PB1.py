# || Jay Shree Radhe Krishna ||
# python is a programming language 
# - created by "guido van rossum" & released in 1991.
# can be used on the server to create web applications.
# can also be used for software development, mathematics, system scripting.  
# can handle big data and  perform complex mathematicn functions. 
# works on windows, mac, raspberry pi, linux etc.)
# rapid prototyping (most importantly).      
# PRINT HELLO WORLD !
print ("Jay Shree Krishna !")
# file handling can be done using python (open, read, write, delete)
# data base can be handled using python (python mysql, python mongoDB)
# latest version is python 3.
# can run using file name.
import sys
print("here is the sys version of the python >> ",sys.version)
# can be directly used from command prompt by typing "python" first and than the other programs.
# python indentation - indentation is must in the python code like  example in this code 
# example - if 5 > 2:
#   print("Five is greater than two!") << indentation is must before print function and if not
# indented than python will consider it as the separate statement (indentation -  space)
# as a programmer 4 spaces is professional else 1 space is compulsory.
#  comments in python 
# 1 
"""
hello there this is multi line string as well as comment in python.
"""

# VARIABLES.
# creating python variables.
a = 5
b = "john"
print(a)
print(b)

c = 7
c = "shaili" # it'll display this line by considering it as latest
print(c)
print(c)
# casting variable 
d = float(10)
e = int(15.5) 
f = str(12334)
print(d, e, f)
# get the type of the value
print(type(d))
print(type(e))
print(type(f)) #even if we give the number still it will consider as string as 'str' is defined.
# single quote or double quote on the value.
g = "krishna"
g = 'radha'
print(g)
print(g)
# case sensitive
H = "radha"
h = 'krishna'
print(H+h) # H will not overwrite h.
#  variable naming conventions
# legal names  
myvar = 10
my_var = 11
_my_var = 12 # basically its an error that displays 
myVar = 13
MYVAR = 14
myvar3 = 16

# illegal names 
# my-var = 15
# my var = 17
# 2myvar = 12
# multiwords variable names
# Camel case
myVariablename = "Krishna"
# Pascal case
MyVariableName = "Radha"
# snake case 
my_variable_name = "radhakrishna"

# Assign multiple values 
# 1 many values to mulitple variables 
i,j,k = "Radha","Krishna","Balram"
print(i)
print(j)
print(k)
# 2 one value to multiple variables 
l = m = n = "radhakrishna"
print (l)
print (m)
print (n)
# unpack a collection 
my_gods = ['radha','krishna','parwati', 'shiv']
[o,p,q,r] = my_gods
print(o)
print(p)
print(q)
print(r)
print(o+p)
print(q+r)
# Global variables
# Variables that are created outside of a function
# (as in all of the examples in the previous pages) are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside. 
# 1 Created a variable outside of a function, and used it inside the function
s = "awesome"

def myfunc():
  print("Python is " + s)

myfunc()

# 2 Created a variable inside a function, with the same name as the global variable
t = "awesome"

def myfunc():
  t = "fantastic"
  print("Python is " + t)

myfunc()

print("Python is " + t)

# The global Keyword
# Normally, when you create a variable inside a function, 
# that variable is local, and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword.
# 3 If you use the global keyword, the variable belongs to the global scope:
def myfunc():
  global u
  u = "fantastic"

myfunc()

print("Python is " + u)

# 4 To change the value of a global variable inside a function,
# refer to the variable by using the global keyword:
v = "awesome"

def myfunc():
  global v
  v = "fantastic"

myfunc()

print("Python is " + v)
# here it won't  consider term 'awesome' and will consider 'fantastic' of the  function.
# todays target is completed.