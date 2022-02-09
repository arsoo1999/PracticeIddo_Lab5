import numpy as np# подключение Numpy

while True:#Цикл While удет работать бесконечно
    try:# защита блока функций от ошибок
        Array = np.random.randint(50, size = (5, 5))# Случайное заполнение матрицы 5 на 5
        Array1 = np.where (Array < 0, 0, Array) #Обнуление всех не положительных значений, если таковые будут в матрице
        Array1 = np.sum (Array1, axis=0)# Суммирование всех столбцов матрицы

        i = 0 # Счетчик
        max = 0# Максимальное число
        J = 0# Индекс максимального числа

        while i != len (Array1): # Цикл работает до конца списка
            if max < Array1[i]: # Проверка на максимальное число
                max = Array1[i]
                J = i
                i = i + 1
            else:
                i = i + 1
    except (KeyboardInterrupt, ValueError):# Проверка на ошибки
        print ("")
    else:# Защита от матрицы заполненной нулями
        if Array[0,0] == 0:
            continue #Повторение цикла
        break #Окончание цикла

print("Исходная матрица\n",Array)#Вывод исходной матрицы в консоль
min = np.amin (Array[:,J]) # Нахождение минимального числа их столбца с самой максимальной суммой абсолютных чисел
print("Минимальный элемент:", min) # Вывод минимального элемента

with open('Practice1.txt', 'wt') as file:# Открытие\создание файла в который будет записаны все результаты обработки
    file.write ("Исходная матрица:\n")
    for row in Array:
        file.write(' '.join([str(a) for a in row]) + '\n')
    file.write ("Минимальный элемент:\n" + str(min))



