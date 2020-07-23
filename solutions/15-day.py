"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
"""
# from random import random
#
# def pick_random(element):
#    pass

from random import random

count_so_far = 0
result = None
arr = []


def pick_random_element(x):
    global count_so_far, result, arr
    count_so_far += 1

    print("Count, result: ",count_so_far, result)

    if count_so_far == 1:
        result = x
    else:
        random_value = int(count_so_far * random())
        print("RAND", random_value)
        if random_value == count_so_far - 1:
            result = x
            arr.append(result)

    print(arr)
    return result


sample_stream = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for index, element in enumerate(sample_stream):
    random_element = pick_random_element(element)
    print("Random element of the first {} is {}".format(index + 1, random_element))
