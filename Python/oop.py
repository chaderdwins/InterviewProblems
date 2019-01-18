#defining a class
class User:
    def __init__(self, first, last, age):
        self.f_name = first
        self.l_name = last
        self.age = age

    def full_name(self):
        return f"{self.f_name} {self.l_name}"

    def initials(self):
        return f"{self.f_name[0]}.{self.l_name[0]}."

    def candy(self, thing):
        return f"{self.f_name} likes {thing}"



#creating an instance of the class UserOne
user1 = User("Chad","Erdwins",22)
# print(user1.f_name, user1.l_name, user1.age)

print(user1.full_name())
print(user1.initials())
print(user1.candy("pizza"))
