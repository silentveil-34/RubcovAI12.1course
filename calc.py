while True:
    print("\n ВЫБЕРИТЕ РЕЖИМ КАЛЬКУЛЯТОРА")
    print("1. Обычный калькулятор")
    print("2. Спортивный калькулятор")
    print("0. Выход из программы")

    mode = input("Выберите режим калькулятора (0-2): ")

    if mode == "0":
        print("Выход из программы. Досвидания!")
        break

    if mode == "1":
        while True:
            print("\n ОБЫЧНЫЙ КАЛЬКУЛЯТОР")
            print("Операции:")
            print("1-сложение")
            print("2-вычитание")
            print("3-умножение")
            print("4-деление")
            print("5-возведение в степень")
            print("6-остаток от деления")
            print("7-целочисленное деление")

            vibor = input("Выберите операцию (0-7): ")

            if vibor == "0":
                break

            if vibor not in ['1', '2', '3', '4', '5', '6', '7']:
                print("Ошибка! Такой операции нет")
                continue

            num1 = int(input('Введите число №1: '))
            num2 = int(input('Введите число №2: '))

            if vibor == "1":
                print("Результат", num1 + num2)
            elif vibor == "2":
                print("Результат", num1 - num2)
            elif vibor == "3":
                print("Результат", num1 * num2)
            elif vibor == "4":
                if num2 != 0:
                    print("Результат", num1 / num2)
                else:
                    print("Деление на ноль невозможно")
            elif vibor == "5":
                print("Результат", num1 ** num2)
            elif vibor == "6":
                if num2 != 0:
                    print("Результат", num1 % num2)
                else:
                    print("Деление на ноль невозможно")
            elif vibor == "7":
                if num2 != 0:
                    print("Результат", num1 // num2)
                else:
                    print("Деление на ноль невозможно")

    if mode == "2":
        while True:
            print("\n СПОРТИВНЫЙ КАЛЬКУЛЯТОР")
            print("1. Сумма очков")
            print("2. Умножение результата на число раундов")
            print("3. Полные серии")
            print("4. Остаток повторений")
            print("0. Выход в главное меню")

            vibor = input("Выберите операцию (0-4): ")

            if vibor == "0":
                break

            if vibor not in ['1', '2', '3', '4']:
                print("Ошибка! Такой операции нет")
                continue

            num1 = int(input('Введите число №1: '))
            num2 = int(input('Введите число №2: '))

            if vibor == "1":
                print("Сумма очков:", num1 + num2)
            elif vibor == "2":
                print("Результат за все раунды:", num1 * num2)
            elif vibor == "3":
                if num2 != 0:
                    print("Полные серии:", num1 // num2)
                else:
                    print("Деление на ноль невозможно")
            elif vibor == "4":
                if num2 == 0:
                    print("Раундов не может быть 0!")
                else:
                    result = num1 % num2
                    print("Остаток повторений:", result)
                    if result > 50:
                        print("Отличный результат!")
