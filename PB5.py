# PYTHON STRINGS 
# single  and double quotes - 
print("Radha")
print('Radha')

# usage of both qoutes in same sentence - 
print("Radha's philosphy - Pane ko hi prem kre jag ki hai ye rit")
print('"o arjun" its diffiucult to control the mind but is possible through proper practise')

# assign string to a variable 
a = "Radha"
print(a)

# multiline strings 
b = '''

असंशयं महाबाहो मनो दुर्निग्रहं चलम् ।
अभ्यासेन तु कौन्तेय वैराग्येण च गृह्यते ॥

Krishna's shloka on focus -
In the Bhagavad Gita, Lord Krishna says that to achieve success, 
one should focus on themselves and their strengths,
rather than others.

'''
print(b)

# strings are arrays 
a = "RadhaKrishn"
print(a[2])
print(a[1:-1])
print(a[0:])
print(a[-7:-2]) #learnt most important thing that is >> index -ve value should be higher to lower
# it won't work if we write [-2 : -7] but will work if we write [-7 : -2] 

#  looping through a string 
for x in "banana":
 print(x)

# string length 
b = "RadhaKrishn"
print(len(b)) # Most important thing -it also counts the space between or both ends of the string.

# check string 
Gita = "Yada Yada Hi Dharmasya Glanirbhavti Bharata"
print("Yada" in Gita) # It checks the string but is case sensitive.
# you have to check by exact word that you have used in the para.

# if statement 
Gita_Updesh = "Yada Yada Hi Dharmasya Glanirbhavti Bharata"
if "Hi" in Gita_Updesh : 
    print("yes, 'Hi' is present")

Gita_Path = "Yada Yada Hi Dharmasya Glanirbhavti Bharata"
if "dharmasya" not in Gita_Path :
    print("Yes but not in small case")

# Methods of  strings 
# 1. Slicing Method 
# slicing
c = "ParwatiShiv"
print(c[1 : 4])

# slice from start
d = "ParwatiShiv"
print(d[:11])

# slice to the end 
e = "ParwatiShiv"
print(e[0:])

# -ve indexing
f = "ParwatiShiv"
print(f[-4 : -2])
# one more time reminder - in case of -ve indexing make sure the bigger number will come first
# like example a[-7 : -2] and it wont display anything if we use a[-2 : -7].
# python considers higher number first incase of -ve indexing
# incase of +ve indexing python won't display output for a[5:2]

# 2. Modify Strings 

# uppercase
g = "  ParwatiShiv  "
print(g.upper())

# lowercase
print(g.lower())

# Remove whitespace 
print(g.strip()) #it removes whitespaces from both the ends of the string.

# replace string 
print(g.replace("w", "v"))
print(g.replace("ParwatiShiv" , "ParwatiShivGaneshKartikey")) #it'll replace the string.

# Split string 
h =  "RadhaKrishn,ShivParwati"
print(h.split(','))

# 4. Concatenate Strings

i = "Radha"
j = "Krishna"
k = i+j
print(k)

l = "Parvati"
m = "Shiv"
n = "Radha"
o = "Krishna"
p = l + m + " > " + n + o
print(p)

# 5. format strings 
q = 3228
r = f"Krishna's birth year is predicted by archealogist on {q} BCE"
print(r)

s = 3228
t = f"Krishna's birth year is predicted by archealogist on {s : .2f} BCE"
print(t)  #some numbers consist 2 decimal points so for same we use .2f and .1f in python.

u = f" After Counting total years completed from krishna's birth till current year ~ {3228 - 2024}"
print(u)

# 6. escape characters 
# Single quote
v = "Radha\'s Krishna & Shiv\'s Parwati"
#this escape character is usefull when double qoutes are to be used in the same string twice.
#like for ex : "Radha\"Krishna\""
print(v)
#  Backslash
w = "RadhaKrishna \\ ParvatiShiv \\ SiyaRam \\ LaxmiNarayan"
print(w)
# Newline
x = "RadhaKrishna\nParvatiShiv\nSiyaRam\nLaxmiNarayan"
print(x)
# carriage return
y = "Radhakrishn\rParwatiShiv"
print(y)
# Tab
z = "RadhaKrishn\tParvatiShiv"
print(z)
# Backslash
A = "Radha Krishna"
print(A)
# Octal value 
B = "\110\145\154\154\157" #its an octal value for 'hello'
print(B)
# hexvalue
C = "\x48\x65\x6c\x6c\x6f" #its an hex value for 'hello'
print(C)

# to be continued...........string methods {please create the new file}



