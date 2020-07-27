"""

Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.
"""
from collections import deque

def get_sub_max(l, k):
    d = deque()
    m = []

    for num, string in enumerate(l):
        if len(d) < k:
            d.append(string)
            pass
        else:
            m.append(max(d))
            d.popleft()
            d.append(string)
    m.append(max(d))

    return m

assert get_sub_max([10, 5, 2, 7, 8, 7], 3) == [10, 7, 8, 8]
assert get_sub_max([5, 2, 1], 2) == [5, 2]



