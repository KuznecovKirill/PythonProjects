import json
from animal import Animal
from mammal import Mammal
from dog import Dog

newAnimal = Animal("Джастин",7,"М")
newMammal = Mammal(newAnimal.name,newAnimal.age,newAnimal.gender,"Обезьяна")
print(newAnimal,newMammal)