"""
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

PASS
"""


def m_sum(array_list, k):
    r = set(map(lambda x: k-x, array_list))
    for i in array_list:
        if i in r and 2*i != k:
            return True
    return False


assert not m_sum([], 17)
assert m_sum([10, 15, 3, 7], 17)
assert not m_sum([10, 15, 3, 4], 17)

