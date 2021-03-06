"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

"""
from functools import reduce

def return_product(arr):
    container = []
    for i, a in enumerate(arr):
        new_list = arr.copy()
        del new_list[i]
        container.append(reduce(lambda x, y: x*y, new_list))
    return container


assert return_product([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert return_product([3, 2, 1]) == [2, 3, 6]
