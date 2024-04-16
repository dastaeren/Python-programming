class Dog:
 def __init__(self, breed, age, color):
    self.breed = breed
    self.age = age
    self.color = color
 def bark(self):
    print("Woof! Woof!")
 def sleep(self):
    print("Zzz...")
 def eat(self):
    print("Nom nom nom!")

my_dog = Dog(breed="Labrador Retriever", age=3, color="Golden")
print(f"My dog is a {my_dog.color} {my_dog.breed} and is {my_dog.age} years old.")
my_dog.bark()
my_dog.sleep()
my_dog.eat()


        
