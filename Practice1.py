val = int(input('Выберите способ заполнения списка: 1 - ручной ввод, 2 - генерация списка:  '))
array = None  # Создание пустой переменной

if val == 1:     # Проверка условия, если пользователь ввел еденицу то производится ниже прописанный функционал
    while True:  # Считывание списка и сохранение в переменной\\Создание цикла, цикл будет продолжаться пока пользователь вводит данные не корректно
        try:     # Создаю конструкцию для обработки исключений
            array = list(map(int, input().split()))  # В переменную записываю список введенный с клавиатуры
            break                                    # При правильном вводе цикл останавливается
        except ValueError:                           # Если функция получает аргумент правильного типа, но несоответствующее значение, то выводится надпись с просьбой ввести заново последовательность цифр.
            print("Пожалуйста, вводите только числа")
elif val == 2:                                                  # Проверка условия, если пользователь ввел двоечку то производится ниже прописанный функционал
    array = [x + y for x in range(1, 7) for y in range(5, 14)]  # Производится генерация при помощи цикла

print("Исходный список: ", array)  # Вывод исходного списка

list_length = len(array) - 1  # Переменная хранящая в себе длину списка, которая в дальнейшем цикле будет меняться в зависимости от динамики размера списка
i = 0

# Удаление цепочек нечетных чисел
while i != list_length:                          # Цикл работает до того момента пока i не равен длине списка a
    chain_size = 0                               # Переменная хранящая в себе размер цепочки нечетных чисел и обнуляется при каждом повторении цикла
    Check = int(array[i]) % 2                    # Переменная проверяющая каждое число четная она или нечетная
    if Check != 0:                               # Если число нечетное то выполняется ниже представленный функционал
        init_index = i                           # Переменная хранит индекс нечетного числа с которого начался цикл
        Final_Index = i                          # Переменная хранит индекс последнего нечетного числа который проверяется в следующем цикле while
        while Check != 0:                        # Если число нечетное то выполняется ниже представленный функционал
            Check = int(array[Final_Index]) % 2  # Переменная проверяющая каждое число четная она или нечетная
            Final_Index = Final_Index + 1        # В переменной хранится индекс проверяемых чисел в данном цикле
            if Check != 0:                       # Если каждое последующее число нечетное, то переменная CellNum увеличивается на еденицу
                chain_size = chain_size + 1
            if Check == 0 and chain_size < 3:                     # Если число в данном цикле четное и цепочка нечетных чисел меньше меньше 3-х
                Final_Index = Final_Index - 1
                del array[init_index:Final_Index]                 # то цепочка нечетных чисел от индекса j до k удаляется из списка
                i = 0                                             # и счетчик основного цикла обнуляется и проверка всего списка начинается с начала
            elif Check == 0 and chain_size >= 3:                  # Если же число в данном цикле четное, но цепочка нечетных чисел больше или равна 3-м
                i = Final_Index - 1                               # то счетчик основного цикла продолжает проверку списка с последнего числа который был проверен на нечетность

    i = i + 1
    list_length = len(array) - 1

print("Обработанный список: ", array) # Вывод обработанного списка