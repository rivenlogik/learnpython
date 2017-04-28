## Animal is-a object (yes, sort fo confusing) look at the extra credit
class Animal(object):

    def check(self):
        print "In animal object!"

## class Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

    def check2(self):
        print "In dog!"

## class Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## class Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## class Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## class Fish is-a object
class Fish(object):
    pass

## class Salmon is-a Fish
class Salmon(Fish):
    pass

## class Halibut is-a Fish
class Halibut(Fish):
    pass

## fluffy is-a Animal
fluffy = Animal()

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a pet
mary.pet = satan

## Frank is-a employee
frank = Employee("Frank", 120000)

## Frank has-a pet
frank.pet = rover

## Flipper is-a fish
flipper = Fish()

## crouse is-a salmon is-a fish
crouse = Salmon()

## harry is-a halibut is-a fish
harry = Halibut()

fluffy.check()
rover.check()
rover.check2()
try:
    fluffy.check2()
except:
    print "Cannot execute check2 Dog() function on fluffy Animal() instance!"
