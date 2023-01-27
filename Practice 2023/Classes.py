class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Hello, my name is " + self.name)

    def have_birthday(self):
        self.age += 1
        print("Happy birthday! I am now " + str(self.age) + " years old.")


person = Person("John", 30)
person.introduce()
person.have_birthday()
