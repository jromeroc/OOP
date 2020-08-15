import abc
from abc import ABCMeta

class Vehicle(object):
    __metaclass__ = ABCMeta
    
    @abc.abstractmethod
    def who_are_you(self):
        print ("I'm a vehicle and also an abstract method")

    def get_color(self):
        pass
    
    def set_color(self, value):
        pass

    color = abc.abstractproperty(get_color, set_color)
        
class Car(Vehicle):

    def __init__(self):
        Vehicle.__init__(self)
        self._color = "red"
        
    def who_are_you(self):
        print("I'm a car")

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

car = Car()
print("I'm a car color {}".format(car.color))
car.color = "blue"
car.who_are_you()
print("Want to be a car color {} ".format(car.color))