class Animal:
    def getAnimal(self):
        print("Cat and Dogs are animals")

class Cat(Animal):
    def getCat(self):
        print("Cat meows")
class Dog(Animal):
    def getDog(self):
        print("Dog barks")

h = Animal()
h.getAnimal()
s = Cat()
s.getCat()
s = Dog()
s.getDog()