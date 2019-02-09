def perm(data):
    if len(data) == 0:
        return [[]]
    li = []
    for index, value in enumerate(data):
        for p in perm(data[:index] + data[index+1:]):
            li.append([value] + p or [[]])
    return li

z = perm(['a','b','c'])
print(z)