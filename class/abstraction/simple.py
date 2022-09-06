import abc
 
class Animal(metaclass=abc.ABCMeta):
 
    @abc.abstractmethod  # class inheritates from Animal must implement screaming
    def screaming(self):
        'Return when animal screaming the sound hear likes'
        return NotImplemented

class Dog(Animal):
    def screaming(self):
        return 'wolf'

dog = Dog()
print(dog.screaming())