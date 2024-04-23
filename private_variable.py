class PrivateAM:
    __name = None
    def __init__(self, name):
        self .__name = name
    def __displayDetails(self):
        print("Name: ",self.__name)
    def accessPrivateFunction(self):
        self.__displayDetails()

obj = PrivateAM("Hello")
obj.accessPrivateFunction()