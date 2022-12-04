def MyMap(func, originalList: list) -> list: #Реализация Map
    newList = list()
    for object in originalList:
        newList.append(func(object))
    return newList