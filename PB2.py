# Python Datatypes 
# Setting the datatype 
# 1 string 
a = "RadhaKrishna"
print(type(a))
print(a)

# 2 integer
b = 10
print(type(b))
print(b)

# 3 Float
c = 14.5
print(type(c)) 
print(c)

# 4 complex
# lets understand this as 'j' is the imaginery unit.
# & 1 is the  imaginery number.
# Pendulum: A swinging pendulum moves to one side, then back to the
# center, and then to the other side, repeating this motion.
# Sound Waves: Air molecules vibrate back and forth to create sound,
# causing pressure changes that travel through the air.
d = 6j
print(type(d))
print(d)

# 5 list
# lists are declared in square brackets 
# lists are mutable {meaning} - add, modify, remove items.
e = ['Radha','Krishna','Parwati','Shiv']
print(type(e))
print(e)

# 6 Tuples
# tuples are declared using parenthesis 
# tuples are immutable {meaning} - can not add, change, remove items.
# tuples are more faster than lists as are immutable that makes them memory efficient.
f = ('Radha','Krishna','Parwati','Shiv')
print(type(f))
print(f)

# 7 Range 
# basically used for displaying the numbers in sequence 
# mostly used in for loops 
g = range(6)
print(type(g))
print(g)
# for z in range(start, stop, step):
    

# 8 Dict
h = {
    "Name" : "Radha",
     "janmashtmi" : 11
    }
print(type(h))
print(h)

# 9 Set
# sets are mutable 
# and are declared in single curly braces 
i = {"Radha","Krishna","Parwati","Shiv"}
print(type(i))
print(i)

# 10 Frozenset
# frozen sets are immutable and declared using parenthesis (1) and curly braces {2}
j = frozenset({"Radha","Krishna","Parwati","Shiv"})
print(type(j))
print(j) 

# 11 Boolean 
k = True
print(type(k))
print(k)

# 12 Bytes
l = b'RadhaKrishna'
print(type(l))
print(l)
# bytes represents the binary data which is not in human readable form.
# each elements in bytes are in integer format that is (0 - 255).
# use case -
# sending and receiving data on network [store network packets]
# audio, video, image file handling 
# its immutable (not modifiable)

# 13 Bytearray
m = bytearray(10)
print(type(m))
print(m)
# its same as bytes, only the difference is...
# its mutable (modifiable).
data = bytearray([65, 66, 67, 68]) #its an ASCII code for abcd
print(data) 

# 14 memoryview
n = memoryview(bytes(15))
print(type(n))
print(n)
# The memoryview data type in Python provides a way to access and manipulate the memory of 
# another binary object (like bytes or bytearray) without creating a copy of the data. 
# This can save memory and improve performance when working with large data sets,
# because instead of copying data, memoryview just references the existing data in memory.

# 15 none
o = None
print(type(o))
print(o)

# Setting the specific data type 
# 1 string
A = str(1234)
print(type(A))
print(A)

# 2 Integer
B = int(20.50)
print(type(B))
print(B)

# 3 Float
C = float(12)
print(type(C))
print(C)

# 4 complex
D = complex(1j)
print(type(D))
print(D)

# 5 list
E = list(("Radha","Krishna","Parwati","Shiv"))
print(type(E))
print(E)

# 6 tuple
F = tuple(("Radha","Krishna","Parwati","Shiv"))
print(type(F))
print(F)

# 7 range
G = range(10)
print(type(G))
print(G)

# 8 dict
H = dict(Name = "Radha", janmashtami = 11)
print(type(H))
print(H)

# 9 set
I = set(("Radha","Krishna","Parwati","Shiv"))
print(type(I))
print(I)

# 10 frozenset
J = frozenset(("Radha","Krishna","Parwati","Shiv"))
print(type(J))
print(J)

# 11 bool
K = bool(1)
print(type(K))
print(K)

# 12 bytes
L = bytes(5)
print(type(L))
print(L)

# 13 bytearray 
M = bytearray(15)
print(type(M))
print(M)

# 14 Memoryview
N = memoryview(bytes(15))
print(type(N))
print(N)



