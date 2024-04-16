class Student:
    def setModules(self, gender):
        self.gender = gender
    def getModules(self):
        return self.gender
    
obj1 = Student()
obj1.setModules("BIA 101")
print(obj1. getModules())
obj2 = Student()
obj2.setModules("BIA 102")
print(obj2.getModules())