import os
import pandas as p
from operator import itemgetter

class animal:
        PathCSV = None
        AnimalDict = None
        def __repr__(self): # Создаем словарь с присвоенными к нему данными с открытого файла
            with open ( self.PathCSV, "r") as f:
                file_reader=p.read_csv ( f , delimiter = ";")
                animal.AnimalDict=file_reader.to_dict('records')

class OperFile(animal):
    PathF = ''
    def __repr__(self): # выводим список файлов по пути PathF
        super().__repr__()
        LenFile = repr(len(os.listdir(path = self.PathF)))
        return LenFile

    def __getitem__(self, item): #Функция для обращения по индексу к словарю
        return self.AnimalDict[item]

    @staticmethod
    def FileOperation():#Автоматичский ввод пути к папке и к файлу
        setattr(OperFile, 'PathF', '.')
        setattr(OperFile, 'PathCSV', "DataBaseAnimal.csv")
        x = OperFile()
        print("Число хранящихся файлов = ",repr(x))  #Вывод количества файлов в папке
    @staticmethod
    def Sorting():# Сортировка
        OperFile.FileOperation()
        x = OperFile()

        x.AnimalDict.sort(key=itemgetter('Животные'))                    #Сортировка по столбцу Животным

        print("\033[32m {}" .format( p.DataFrame( x.AnimalDict ) ) , "\n" )

        x.AnimalDict.sort(key=itemgetter('№'))                          #Сортировка по столбцу номера
        print("\033[31m {}" .format( p.DataFrame( x.AnimalDict ) ) , "\n" )


class Iter(OperFile):
    @staticmethod
    def FilterDF():
        x = OperFile()
        for d in reversed ( range ( len ( x.AnimalDict ) ) ):  # Перебор словаря снизу вверх
                if x.AnimalDict[d]['№'] > 6:                   # Если номер равен 6-ти
                  del x.AnimalDict[d]                          # удаляем строку учавствующую в данном цикле
        AnimalDict = p.DataFrame(x.AnimalDict)                 # Словарь конвертируем в DataFrame
        print ( "\033[34m {}".format ( AnimalDict ) , "\n" )   # Вывод результата
        return AnimalDict
    @staticmethod
    def CsvRecording():
        OperFile.Sorting ()
        Iter.FilterDF().to_csv('SortDataBaseAnimal_P4.csv', index = False )  # Запись в существующий/созданный файл .csv


Iter.CsvRecording()        #обращение к функции из класса Iter


