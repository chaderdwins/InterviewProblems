#defining a class
class User:
    def __init__(self, first, last, age):
        self.f_name = first
        self.l_name = last
        self.age = age



#creating an instance of the class UserOne
user1 = User("Chad","Erdwins",22)
print(user1.f_name, user1.l_name, user1.age)
