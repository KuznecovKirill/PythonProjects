import json
from mammal import Mammal
class Dog(Mammal):
    def __init__(self, name = "", age = 0, gender = "", viewDog = ""):
        super().__init__(name,age,gender,"Собака")
        self.viewDog = viewDog
    def __repr__(self)->str:
        return self.__str__()
    def __str__(self) -> str:
        return str(self.__dict__)
    