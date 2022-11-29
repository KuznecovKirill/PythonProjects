class Animal:
    def __init__(self, name = "", age = 0, gender = ""):
        self.name = name
        self.age = age
        self.gender = gender
    def __repr__(self): # отображение объекта в режиме отладки
        return self.__str__()