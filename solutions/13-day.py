"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""
from collections import Counter

def get_longest_substring(s, k):
    word_list = []
    if k == 1:
        return s[0]
    for num, w in enumerate(s):
        for i in range(num+1, len(s)+1):
            if len(Counter(s[num:i])) < k:
                pass
            elif len(Counter(s[num:i])) == k:
                word_list.append(s[num:i])
            else:
                break
    word_list_len = [len(w) for w in word_list]

    return word_list[word_list_len.index(max(word_list_len))]



assert get_longest_substring("abcba", 2) == "bcb"
assert get_longest_substring("abccbba", 2) == "bccbb"
assert get_longest_substring("abcbbbabbcbbadd", 2) == "bbbabb"
assert get_longest_substring("abcbbbaaaaaaaaaabbcbbadd", 1) == "a"
assert get_longest_substring("abccbba", 3) == "abccbba"
