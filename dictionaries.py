dict = {
    'apples': 7,
    'oranges': 12,
    'grapes': 5
}

# to get an item from a dictionary
apples = dict.get('apples')  # option 1
apples1 = dict['apples']  # option 2

print(apples1)


# add items to the dict
dict['banana'] = 4

print(dict)


# remove items from the dict
dict.popitem()  # removes last item from dict
print(dict)
dict.pop('oranges')
print(dict)
