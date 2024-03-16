import csv

def readCsv(file_path):
    """Позволяет прочитать csv файл
        и возвращает массив, содержащий словари,
        которые представляет собой содержание строк
        csv

        Аргументы:
        file_path -- Путь к файлу"""
    table =[]
    with open(file_path, "r", encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=',')
        for i in reader:
            table.append(i)
    return table

def write_txt(table, file_path):
    """Позволяет записать txt файл
        в формате "<magicaPotions> в запасах еще есть - <count>"
        Заменяет все значения в ячейке "count" -1 на 0

        Аргументы:
        table - массив, содержащий словари с данными
        file_path -- Путь к новому файлу"""
    with open(file_path, mode="w", encoding='utf-8') as file:
        for i in table:
            file.write(i["magicaPotions"] + " в запасах еще есть - " + (i["count"] if i["count"] != "-1" else "0") + '\n')

def count_all(table):
    """Объединяет повторяющиеся строки
        в массиве, содержащем словаре по
        ключу "magicaPotions".

        Аргументы:
        table -- массив, содержащий словари с данными
        """
    indexes = []
    A = []
    for i in table:
        if (dictElemInArray(A, i["magicaPotions"])) == -1:
            A.append(i)
        else:
            A[dictElemInArray(A, i["magicaPotions"])]["count"] = str(int(A[dictElemInArray(A, i["magicaPotions"])]["count"]) + int(i["count"]))
    return A


def dictElemInArray(A, dict_elem):
    """Находит элемент словаря в массиве

        Аргументы:
        A - массив
        dict_elem - элемент словаря
    """
    for i in range(len(A)):
        if A[i]["magicaPotions"] == dict_elem:
            return i
    return -1


# Читаем csv таблицу
table_potions = readCsv("C:/Users/kids01/Desktop/Вариант 29/magical.csv")

# Подсчитываем общее количество
all_potions = count_all(table_potions)

potion_classes = dict()
for i in all_potions:
    # Определяем имя класса зелья
    if len(i["magicaPotions"].split()) == 3:
        class_name = i["magicaPotions"].split()[1] + ' ' + i["magicaPotions"].split()[2]
    else:
        class_name = i["magicaPotions"].split()[1]

    # Записываем имя класса словарь potion_classes в
    # качестве ключа, а в качестве значения - массив,
    # содержащий уникальные имена зелий и их общее количество
    if class_name not in potion_classes.keys():
        potion_classes[class_name] = [[i["magicaPotions"]],int(i["count"])]
    else:
        if str(i["magicaPotions"]) not in potion_classes[class_name][0]:
            potion_classes[class_name][0] += [str(i["magicaPotions"])]
        potion_classes[class_name][1] += int(i["count"])

for i in range(len(potion_classes)):
    print(len(list(potion_classes.values())[i][0]), "зелий класса", list(potion_classes.keys())[i], "общее количество зелий", list(potion_classes.values())[i][1])
