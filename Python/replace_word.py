def find_and_replace(name, word, rep):
    with open(name, "r+") as file:
        change = file.read().replace(word, rep)
        file.seek(0)
        file.write(change)
    return True
    
print(find_and_replace("story.txt", "canary", "thesis"))
