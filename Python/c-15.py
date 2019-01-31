# Write a function called includes which accepts a collection, a value, and an
# optional starting index.The function should return True if the value exists
# in the collection when we search starting from the starting index.
# Otherwise, it should return False.
#
# The collection can be a string, a list, or a dictionary. If the collection
# is a string or array, the third parameter is a starting index for where to search
# from. If the collection is a dictionary, the function searches for the value among
# values in the dictionary; since objects have no sort order, the third parameter is ignored.

def includes(collection, value, start_index=0):
    if type(collection) == type({}):
        return value in collection.values()
    return value in collection[start_index:]
