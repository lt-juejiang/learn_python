#!/user/bin/python
#coding=utf-8
class Animal(object):
    def T_print(self):
        print("Animal");

class Mammal(Animal):
    def T_print(self):
        print("Mammal");

class Bird(Animal):
    def T_print(self):
        print("Bird");

class Parrot(Bird):
    def T_print(self):
        print("Parrot is Bird");

class Ostrich(Bird):
    def T_print(self):
        print("Ostrich is Bird");

class MixlnRunning(object):
    def run(self):
        print("Running....");

class MixlnFlying(object):
    def fly(self):
        print("Flying....");

class Dog(Mammal,MixlnRunning):
    def T_print(self):
        print("Dog is Mammal Animal");

class Bat(Mammal,MixlnFlying):
    def T_print(self):
        print("Bat is Mammal Animal");

dog = Dog();
bat = Bat();
dog.T_print()
dog.run()