#love calculator
from ipaddress import v4_int_to_packed


print("Welcome to Love Calculator")
name1 = input("Enter firts name: \n")
name2 = input("Enter second name: \n")

combined_name = name1 + name2
print(combined_name)
noms_minuscules = combined_name.lower()

t = noms_minuscules.count("t")
r = noms_minuscules.count("r")
u = noms_minuscules.count("u")
e = noms_minuscules.count("e")

true = t + r + u + e

print(true)

l = noms_minuscules.count("l")
o = noms_minuscules.count("o")
v = noms_minuscules.count("v")
e = noms_minuscules.count("e")

love = l + o + v + e

print(love)

love_index =  str(true) + str(love)

print (love_index)

