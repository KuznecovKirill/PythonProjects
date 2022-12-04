import csv
import random
FILENAME: str = "DataSet.csv" # файл с изначальными данными
OUTFILE: str = "NewDataSet.csv" # файл с преобразованными данными

def FillDataSet() -> list:
    breed: list = ["Мопс","Пудель","Английский бульдог","Долматинец","Чау-чау","Бигль","Доберман"]
    name: list = ["Олег", "Лео","Барни","Тайсон","Локи","Нора","Рекс","Рокки"]
    country: list = ["(Россия)","(Франция)","(Англия)","(США)","(Китай)","(Нидерланды)","(Швеция)"]
    Dog = list()
    i: int = 0
    countDog: int = 40
    Dog.append(["Собака","Возраст"])
    while i < countDog:
        randomDog = breed[random.randint(0, len(breed) - 1)] + " " + name[random.randint(0, len(name) - 1)] + " " + country[random.randint(0, len(country) - 1)]
        Dog.append([randomDog, random.randint(0,11)])
        i += 1
    return Dog

def WriteInCSV(dataSet: list, fileName: str):
    with open(fileName, "w", newline="") as file:
        wr = csv.writer(file, delimiter=';')
        wr.writerow(dataSet)

def SplitDog(originalDict: dict) -> dict: #Разделение первого столбца на 3 новых
    newDict = dict()
    strs = originalDict["Собака"].split(' ')
    newDict["Порода"] = strs[0]
    newDict["Имя"] = strs[1]
    newDict["Родина"] = strs[2]
    newDict["Возраст"] = originalDict["Возраст"]
    return newDict


WriteInCSV(FillDataSet(), FILENAME) # заполнение таблицы

