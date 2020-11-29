#!/usr/bin/python3
# Calculate the square root of a number using Newton's Method of Approximating the Square
def SQRT(a):
    # guess = a/3
    a = float(a)

    Xn = 1.0  # Initial Guess
    iter = 60  # Number of iterations
    i = 0
    while i < iter:
        Xn = 0.5 * (Xn + a / Xn)
        print(Xn)
        i = i + 1
    print("done")
    print(a)


SQRT(200.0000)
