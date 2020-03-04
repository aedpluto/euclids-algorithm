"""
Euclid's algorithm
"""
import time

def euclid(num1, num2, displayCalculations=False):
    numbers = [num1, num2]
    while numbers[-1] != 0:
        numbers.append(numbers[-2] % numbers[-1])
        if displayCalculations:
            time.sleep(1)
            print(numbers)
    return numbers[-2]
