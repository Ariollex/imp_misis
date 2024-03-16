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

def find_potion(table, name):
    """Находит и выводит оставшееся
        количество зелья

        Аргументы:
        table -- массив, содержащий словари с данными
        name -- имя зелья"""
    for i in table:
        if i["magicaPotions"] == name:
            print("Данного зелья осталось -", i["count"])

# Читаем csv таблицу
table_potions = readCsv("C:/Users/kids01/Desktop/Вариант 29/magical.csv")
# Подсчитываем общее количество
all_potions = count_all(table_potions)
# Записываем в txt
write_txt(all_potions, "C:/Users/kids01/Desktop/Агапкин Артем Дмитриевич 1375/magicaPotions.txt")
# Находим "Мощное Зелье"
find_potion(all_potions, "Мощное Зелье")
