import json
from pprint import pprint
from animal import Animal, AnimalSerialize
from mammal import Mammal
from dog import Dog

newAnimal = Animal("Джастин",7,"М")
newMammal = Mammal("Лео",4,"М","Обезьяна")
newDog = Dog("Жанна",7,"Ж","Пудель")
print(newAnimal)
print(newMammal)
print(newDog)
AnimalSerialize(newAnimal,"primer.json")