#!/usr/bin/python3

from intfloat import *
from decimal import *
from fractions import *

a = Fraction (321)
b = Fraction (123)
c = Fraction (345, 87)
d = Fraction (3, 77)

z = IntFloat ()
print (z, z.periodic())

z = IntFloat (a)
print (z, z.periodic())

z = IntFloat (a, 3)
print (z, z.periodic())

z = IntFloat (a, -4)
print ("z =", z)
z.negate()
print ("-z","=", z)

x = IntFloat (a, 3)
y = IntFloat (b, -14)
z = x+y
print (x, "+", y, "=", z)

x = IntFloat (a, 3)
y = IntFloat (b, -14)
z = x*y
print (x, "*", y, "=", z)

x = IntFloat (a, 3)
y = IntFloat (b, -14)
z = x/y
print (x, "/", y, "=", z)

z = IntFloat(d)
z += IntFloat(Fraction(19,3))
print (z, "=" , z.periodic())

