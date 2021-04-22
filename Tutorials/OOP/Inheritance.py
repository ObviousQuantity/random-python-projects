class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what I say")

class Cat(Pet):
    def __init__(self,name,age,color):
        super().__init__(name,age) #Super = the class we inherit from
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

class Dog(Pet):  
    def speak(self):
        print("Bark")

class Fish(Pet):
    pass

p = Pet("Dom",17)
#p.speak()
#p.show()

c = Cat("Bill",34,"Brown")
#c.speak()
c.show()

d = Dog("Jill",25)
#d.speak()
#d.show()

f = Fish("Bubbles",10)
#f.speak()
