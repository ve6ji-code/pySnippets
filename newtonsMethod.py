#!/usr/bin/python3
# Calculate the square root of a number using Newton's Method of Approximating the Square
def SQRT(myValue):
    """Calculate the Square root of a given number: myValue"""
    a = float(myValue)          # cast as float
    epsilon = 0.0000000001      # Set your desired precision
    x_old_estimation = a-(a/4.0)  # Initial Guess - Play with this
    iter = 60                   # Number of iterations
    i = 0
    print('Calculating the square root of : {}'.format(myValue))
    while i < iter and x_old_estimation > 0.0:
        # Formula for estimating x of x^2
        x_new_estimation = 0.5 * (x_old_estimation + a / x_old_estimation)
        diff = abs(x_old_estimation - x_new_estimation)
        if diff < epsilon:  # Check to see if epsilon has been met
            break  # Break oput of while loop
        x_old_estimation = x_new_estimation  # set old estimate value
        print('Iteration {} : {}'.format(i, x_new_estimation))
        i = i + 1

SQRT(12349995.6)  # myValue
