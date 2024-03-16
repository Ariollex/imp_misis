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

def find_most_often_potion(table, name):
    """Находит и возвращает словарь
        с данными о зелье с травами с самым большим
        количеством в аптеках с magic_herbs_3 = name.

        Аргументы:
        table -- массив, содержащий словари с данными
        name -- название травы"""
    max_count= -1
    dict_elem = None
    for i in table:
        if i["magic_herbs_3"] == name:
            if int(i["count"]) > max_count:
                max_count = int(i["count"])
                dict_elem = i
    return dict_elem

# Читаем csv таблицу
table_potions = readCsv("C:/Users/kids01/Desktop/Вариант 29/magical.csv")

s = input()
while s != "СТОП":
    elem = find_most_often_potion(table_potions, s)
    if elem is not None:
        print("По вашему запросу", s, "найден следующий вариант:", s, "используется в", elem["magicaPotions"], ", его количество составляет :", elem["count"])
    else:
        print("Такую траву мы не используем")
    s = input()
    
