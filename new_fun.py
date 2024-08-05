class Person():
    def __init__(self,name, age):
        self.name =age
        self.age = age

    def say(self):
        print("My name is {} and I'm {} years old".format(self.name,self.age))


p1 = Person("Kai",25)

p1.say()