"""

Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""

def search_string(string, array):

    bunch_query = dict()
    for word in array:
        for num, w in enumerate(word):
            if not bunch_query.get(word[:num+1], None):
                bunch_query[word[:num+1]] = [word]
            else:
                bunch_query[word[:num+1]].append(word)

    return bunch_query.get(string, [])


assert search_string("de", ["dog", "deer", "deal"]) == ['deer', 'deal']
assert search_string("de", ["dog", "deer", "deal"]) == ["deer", "deal"]
assert search_string("ca", ["cat", "car", "cer"]) == ["cat", "car"]
assert search_string("ae", ["cat", "car", "cer"]) == []
assert search_string("ae", []) == []


