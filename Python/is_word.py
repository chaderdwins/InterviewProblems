def is_word(string):
    perms = permutations(string)
    with open('dictionary.txt', 'r') as file:
        li = file.readlines()
        for item in perms:
            if item + '\n' in li:
                print(item)
    return False


def permutations(word):
    if len(word) == 1:
        return [word]
    perms = permutations(word[1:])
    print(perms)
    char = word[0]
    result = []
    for perm in perms:
        for i in range(len(perm) + 1):
            result.append(perm[:i]+char+perm[i:])
    return result

print(is_word('abc'))
