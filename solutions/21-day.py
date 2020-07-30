"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""

def minimum_rooms(arr):

    if not arr: return 0

    D = {}
    for v in arr:
        D[v[0]] = D[v[0]]+1 if v[0] in D else 1
        D[v[1]] = D[v[1]]-1 if v[1] in D else -1
    sorted_event = sorted(D.items())
    max_rooms = 0
    rooms = 0
    for k, v in sorted_event:
        rooms += v
        print(k, v, rooms)
        if rooms > max_rooms: max_rooms = rooms
    return max_rooms
    print(sorted_event)


# assert  minimum_rooms([]) == 0
# assert  minimum_rooms([(30, 75), (0, 50), (60, 150)]) == 2

def minimum_rooms_2(arr):
    max_rooms = 0
    for v in arr:
        rooms = 1
        for u in arr:
            if u[0]>v[0] and u[0]<v[1]:
                rooms += 1
            print(v, u, rooms)

        if rooms > max_rooms: max_rooms = rooms
    return max_rooms


assert  minimum_rooms_2([]) == 0
assert  minimum_rooms_2([(30, 75), (0, 50), (60, 150)]) == 2

## I have studed this problem via https://gist.github.com/folksilva/46a756979a4b4cedc841fbeb3193f181
