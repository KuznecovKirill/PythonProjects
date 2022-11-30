import json
from pprint import pprint
from animal import Animal, AnimalSerialize, AnimalDeserialize
from mammal import Mammal, MammalSerialize, MammalDeserialize
from dog import Dog, DogSerialize, DogDeserialize

newAnimal = Animal("Джастин",7,"М")
newMammal = Mammal("Лео", 4, "М", "Обезьяна")
newDog = Dog("Жанна",7,"Ж","Пудель")
print(newAnimal)
print(newMammal)
print(newDog)
#Сериализация/десериализация Animal
AnimalSerialize(newAnimal,"primer.json")
newAnimal2 = AnimalDeserialize("primer.json")
pprint(newAnimal2.__dict__)
#Сериализация/десериализация Mammal
MammalSerialize(newMammal,"primer2.json")
newMammal2 = MammalDeserialize("primer2.json")
pprint(newMammal2.__dict__)
#Сериализация/десериализация Dog
DogSerialize(newDog,"primer3.json")
newDog2 = DogDeserialize("primer3.json")
pprint(newDog2.__dict__)


