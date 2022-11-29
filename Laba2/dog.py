import json
from mammal import Mammal
class Dog(Mammal):
    def __init__(self, name = "", age = 0, gender = "", view = "", viewDog = ""):
        self.name = name
        self.age = age
        self.gender = gender
        self.view = view
        self.viewDog = viewDog