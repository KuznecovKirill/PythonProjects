import json
from animal import Animal
class Mammal(Animal):
    def __init__(self, name = "",age = 0,gender = "", view =""):
        super().__init__(name,age,gender)
        self.view = view
    def __repr__(self): # отображение объекта в режиме отладки
        return self.__str__()
    def __str__(self):
        return str(self.__dict__)
   
