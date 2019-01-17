def interleave(x,y):
    # k = zip(x,y)
    # new_string = ''
    # for item in k:
    #     new_string += ''.join(item)
    # return new_string

    ''.join(item) for item in zip(x,y)

print(interleave('hi','ha'))
