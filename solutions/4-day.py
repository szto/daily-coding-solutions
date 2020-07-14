"""
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.

"""

def find_min_int(ar):
    fl = list(filter(lambda x: x > 0, ar))
    if not fl:
        return 1
    sorted_fl = sorted(fl)
    for i in range(1, max(sorted_fl)):
        if not i in sorted_fl:
            return i
    return max(sorted_fl) + 1


assert find_min_int([3,4,-1,1]) == 2
assert find_min_int([1,2,0]) == 3
assert find_min_int([1, 2, 5]) == 3
assert find_min_int([1]) == 2
assert find_min_int([-1, -2]) == 1
assert find_min_int([]) == 1
