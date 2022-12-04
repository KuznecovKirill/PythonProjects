import csv
import random
FILENAME: str = "DataSet.csv" # файл с изначальными данными
OUTFILE: str = "NewDataSet.csv" # файл с преобразованными данными

def FillDataSet() -> list:
    breed: list = ["Мопс","Пудель","Английский бульдог","Долматинец","Чау-чау","Бигль","Доберман"]
    name: list = ["Олег", "Лео","Барни","Тайсон","Локи","Нора","Рекс","Рокки"]
    country: list = ["Россия","Франция","Англия","США","Китай","Нидерланды","Швеция"]
    Dog = list();
    i: int = 0
    countDog: int = 40
    Dog.append(["Собака и её родина","Возраст"])
    while i < countDog:
        randomDog = breed[random.randint(0, len(breed) - 1)] + " " + name[random.randint(0, len(name) - 1)] + " " + country[random.randint(0, len(country) - 1)]
        Dog.append([randomDog, random.randint(0,11)])
        i += 1
    return Dog
