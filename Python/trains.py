class Train:
    def __init__(self, num_cars):
        self.num_cars = num_cars

    def __print__(self):
        return self.num_cars + " car" + " train"

    def __len__(self):
        return self.num_cars

k = Train(4)
print(len(k))
