def in_dict(li):
    is_word = []
    with open("dictionary.txt", 'r') as file:
        words = file.readlines()
        for item in li:
            if ''.join(item) not in is_word:
                if ''.join(item) + '\n' in words:
                    is_word.append(''.join(item))
    return is_word


def perm(data):
    if len(data) == 0:
        return [[]]
    li = []
    for index, value in enumerate(data):
        for p in perm(data[:index] + data[index + 1:]):
            li.append([value] + p  or [[]])
    return li

array = []
usr = input("Please enter a word or number sequence:")
for char in usr:
    array.append(char)
ans = perm(array)
ans = in_dict(ans)
print(ans)
