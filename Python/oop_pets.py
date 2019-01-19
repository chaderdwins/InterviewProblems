class Pet:
    valid_types = ["dog","cat","fish","rodent","lizard","turtle","bird"]
    def __init__(self, name, type):
        if type not in Pet.valid_types:
            raise ValueError(f"You can't have a pet {type}!")
        self.name = name
        self.type = type

pet1 = Pet("Yellow","cat")
pet2 = Pet("Boris", "dog")
# pet3 = Pet("DOOM","Hellhound")
