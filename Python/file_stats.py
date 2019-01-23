def statistics(name):
    with open(name) as file:
        line = file.readlines()
        file.seek(0)
        word = file.read().split()
        file.seek(0)
        char = file.read()
    d = dict(lines=len(line), words=len(word), characters=len(char))
    return d
