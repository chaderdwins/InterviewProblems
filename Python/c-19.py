# Write a function called range_in_list which accepts a list and start and end indices,
# and returns the sum of the values between (and including) the start and end index.

# If a start parameter is not passed in, it should default to zero. If an end
# parameter is not passed in, it should default to the last value in the list.
# Also, if the end argument is too large, the sum should still go through the end of the list.

def range_in_list(li, start=0, end=None):
    if end == None:
        end = li[-1]
    sum = 0
    for item in li[start:end+1]:
        sum += item
    return sum
