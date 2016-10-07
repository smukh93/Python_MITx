"""
animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
print(animals)
"""

animals = {'a': [4, 2, 7, 5, 7, 6], \
'c': [18], 'b': [10, 20, 14, 6, 13, 15, 13, 18, 4, 3],\
'd': [13, 13, 20]}

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    result = 0
    for value in aDict.values():
        result+=len(value)
    return result
print(how_many(animals))

def biggest(aDict):
    result = 0
    max_len = 0
    for key in aDict:
        result = len(aDict[key])
        max_len = max(result,max_len)
    return max_len
print(biggest(animals))

def howManyKey(aDict):
    result = 0
    for key in aDict:
        result += len(aDict[key])
    return result
print (howManyKey(animals))