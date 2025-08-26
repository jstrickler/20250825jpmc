from abc import ABCMeta, abstractmethod

class Dog(metaclass=type):
    pass

class MyBaseClass(metaclass=ABCMeta):

    @abstractmethod
    def spam(self):
        pass

    @abstractmethod
    def ham(self, a, b, c):
        pass

    def cheese(self):
        print("cheese")

class MyConcreteClass(MyBaseClass):
    def spam(self):
        print("spam!")

    def ham(self):
        print("ham!")

mcc = MyConcreteClass()
