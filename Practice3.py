import os
import pandas as p
from operator import itemgetter

def PathFileLen():
    files = os.listdir(path = ".")                                              # Берем список файлов хранящиеся по заданно му пути
    print("Число хранящихся файлов = ","\033[31m {}" .format(len(files)),"\n")  # Выводим число хранящихся в нем файлов
PathFileLen()

def CreateDict():
    with open( "DataBaseAnimal.csv" , "r" ) as f:          #Открываем файл с данными
        file_reader = p.read_csv(f, delimiter = ";")       #Создаем Reader'a через Pandas
        res=file_reader.to_dict ('records')                #Создаем словарь с присвоенными к нему данными с открытого файла
        return res
CreateDict()

def SortingAge():
    res = CreateDict()
    res.sort(key=itemgetter('Возраст'))                     #Сортирует по возврасту животного
    print("\033[32m {}" .format(p.DataFrame(res)),"\n")     #Вывод результата
SortingAge()

def SortingNum():
    res = CreateDict()
    res.sort(key=itemgetter('№'))                            #Сортирует по номеру животного
    print("\033[31m {}" .format(p.DataFrame(res)),"\n")      #Вывод результата
SortingNum()

def Filter():
    res = CreateDict()
    for x in reversed(range(len(res))):#Перебор словаря снизу вверх
        if res[x]['№'] == 6:           #Если номер животного равен 6-ти
            del res[x]                 #удаляем строку учавствующую в данном цикле
    res=p.DataFrame ( res )  # Словарь конвертируем в DataFrame
    print ( "\033[34m {}".format ( res ) , "\n" )  # Вывод результата
Filter()

def RecordingCsv():
    res = CreateDict()
    res.to_csv('SortDataBaseAnimal_P3.csv',index = False)      #Запись в существующий/созданный файл .csv