#Object Oriented Programming (OOP)
#https://www.youtube.com/watch?v=JeznW_7DlB0

class Dog:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self,age):
        self.age = age

d = Dog("Dom",5)
d.set_age(10)
print(d.get_age()) #d gets kind of invisibly passed which is the self param


