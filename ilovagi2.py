class Person:
    def __init__(self, name, likes, hates):
        self.name = name
        self.likes = likes
        self.hates = hates
    def taste(self, food):
        if food in self.likes:
            return f"{self.name} eats the {food} and likes it!"
        elif food in self.hates:
            return f"{self.name} eats the {food} and hates it now!"
        else:
            return f"{self.name} eats the {food}!"

person1 = Person("Sam", ["ice-cream"], ["carrots"])
print(person1.taste("carrots"))
