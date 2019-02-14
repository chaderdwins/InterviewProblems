def perm(data):
    if len(data) == 0:
        return [[]]
    li = []
    for index, value in enumerate(data):
        for p in perm(data[:index] + data[index + 1:]):
            li.append([value] + p or [[]])
    return li

user_in = input("Please enter a word and I will give you the permutations of that word:")
op = []
for char in user_in:
    op.append(char)
for word in perm(op):
    print(''.join(word))

