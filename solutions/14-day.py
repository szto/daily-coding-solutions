"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
"""
import random


def like_pi(num):
    count = 0
    radius = 2
    for _ in range(num):
        x = random.random() * radius
        y = random.random() * radius
        if x ** 2 + y ** 2 < radius ** 2:
            count += 1
    return round(4 * count / num, 3)


print(like_pi(100))
print(like_pi(1000))
print(like_pi(10000))
print(like_pi(100000))
print(like_pi(1000000))
print(like_pi(10000000))
print(like_pi(100000000))
