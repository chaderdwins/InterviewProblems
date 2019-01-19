#defining a class
class User:
    #defining a class attribute
    active_users = 0

    #define a class method
    @classmethod
    def display_users(cls):
        print(cls)

    def __init__(self, first, last, age):
        #instance attributes
        self.f_name = first
        self.l_name = last
        self.age = age
        #accessing and incrementing the class attribute
        User.active_users += 1

    def __repr__(self):
        return f"{self.f_name} is {self.age}"

    #instance methods (fxns)
    def full_name(self):
        return f"{self.f_name} {self.l_name}"

    def initials(self):
        return f"{self.f_name[0]}.{self.l_name[0]}."

    def candy(self, thing):
        return f"{self.f_name} likes {thing}"



#creating an instance of the class UserOne
user1 = User("Chad","Erdwins",22)
# print(user1.f_name, user1.l_name, user1.age)

# print(user1.full_name())
# print(user1.initials())
# print(user1.candy("pizza"))

#printing the class attribute active_users
# print(User.active_users)

# print(User.display_users)

#defined __repr__, seeing the results
print(user1)
