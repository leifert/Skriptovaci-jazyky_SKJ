

import math
import numpy as np

def my_counter(str):
    str = str.lower()
    str = str.replace(" ", "")
    my_dict = {}
    vowels = 'aeiou'
    for char in str:
        if char not in vowels:
            my_dict.setdefault(char, 0)
            my_dict[char] = my_dict[char] +1
    return my_dict
print(my_counter("Technicka univerzita Ostrava"))


def palindrom(str):
    return str == str[::-1]

print(palindrom("jelenovipivonelej"))
print(palindrom("nalijpivo"))


def polynomial(x):
    return x**3 + 3*x**2 - x + 4


print(polynomial(1.0))
print(polynomial(-1.5))

def rectangle(a,b):
    return a*b

def triangle(a,b):
    return a*b/2

print(rectangle(2,4))
print(triangle(2,4))

def approx(f,x1,x2,step):
    my_res = 0
    for i in np.arange(x1, x2, step):
        my_res += rectangle(step, f(i))
        my_res += triangle(step, f(i + step) -f(i))
    return my_res

print(approx(math.sin,0.0,math.pi,math.pi/100))
print(approx(polynomial,0.0,2.0,0.001))


"""
(1)
"Technicka univerzita Ostrava" -> {'t': 3, 'c': 2, 'h': 1, 'n': 2, 'k': 1, 'v': 2, 'r': 2, 'z': 1, 's': 1}


(2) 
"jelenovipivonelej" -> True
"nalijpivo" -> False

(3)
1.0 -> 7.0
-1.5 -> 8.875

(5)
f = math.sin, x1 = 0.0, x2 = math.pi, step = math.pi/100 -> cca 2
f = polynom z (3), x1 = 0.0, x2 = 2.0, step = 0.001 -> cca 18
"""
