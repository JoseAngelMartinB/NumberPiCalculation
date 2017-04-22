#!/usr/bin/python
#!/usr/bin/python # -*- coding: utf-8 -*-

# Calculation of the number PI using Montecarlo Method
# Author: José Ángel Martín Baos
# https://github.com/JoseAngelMartinB

import random
from time import time

N = 10**6 # Number of random points to shoot
R = 1 # Circle Radius
random.seed(int(time()))
c = 0 # Number points inside the Circle
repetitions = 100 # Number of times the method will be repeated
pi_values = [] # List with the values of pi obtained
pi = 0
pi_err = 0

for i in range(0,repetitions):
    print("Repetition %d" % (i + 1))
    for j in range(0, N):
        x = random.random()
        y = random.random()

        x = x * R
        y = y * R

        if x*x + y*y < R*R:
            c += 1

    pi_values.append(4*float(c)/float(N))
    c = 0

for i in range(0,repetitions):
    pi = pi_values[i]/repetitions + pi

for i in range(0,repetitions):
    pi_err =  pi_err + ((pi - pi_values[i])**2)/repetitions

pi_err = pi_err**0.5

print("Pi = %.20f, Error = %.20f" % (pi, pi_err))
