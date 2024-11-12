# Operators in python 
# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

# 1. Arithmatic operators 
a = 10
b = 5
c = a + b
d = a - b
e = a * b
f = a / b
g = a % b
h = a ** b
i = a // b
print("Addition", c) 
print("Substraction", d) 
print("Multiplication", e) 
print("True division", f) # Results  quotient of the division with decimal (floating) point.
print("Modulo division", g) # Results remainder after division as the result. 
print("Exponentiation", h) # It calculates above ex : a to the power of b. 
print("Floor division", i) # Results quotient without decimal point and the final figure.

# 2. Assignment operators 
j = 10 
print(j)
k =20
k += 5 # x = x + 5 ; here k +=5 is written in short as the syntax should be shorter.
print(k)
l = 20
l -= 5 # x = x - 5
print(l)
m = 20
m *= 5 # x = x * 5
print(m)
n = 20
n /= 5 # x = x / 5
print(n)
o = 20
o %= 5 # x = x % 5
print(o)
p = 20 
p //= 5 # x = x // 5
print(p)
q = 20
q **= 5 # x = x ** 5
print(q)
r = 20
r &= 5 # x = x & 5 
print(r)
s = 20
s |= 5 # x = x | 5
print(s)
t = 20
t ^= 5 # x = x ^ 5
print(t)
u = 20 
u >>= 5 # x = x >> 5
print(u)
v = 20
v << 5 # x = x << 5
print(v) 
w = 20
(w := 5) #it needs parenthesis or else will throw an error.
print(w)
