from typing import Union


def x(var: str, t: Union[int, oct, bin, hex]):
    for i in var:
        if i.isalpha():
            return "Ошибка!\nИмеется буква"
    if t != Union[int]:
        return t(int(var))[2:]
    return int(var)


x1 = input(
    "Выберите систему счисления:\n1) Десятичная (10-ичная)\n2) Восьмиричная (8-ичная)\n3) Двоичная (2-ичная)\n4) Шестнадцатиричная (16-ичная)\nВведите номер выбранной опции: ")

match x1:
    case "1":
        x2 = input("Введите число: ")

        print(x(x2, int))

    case "2":
        x2 = input("Введите число: ")

        print(x(x2, oct))
    case "3":
        x2 = input("Введите число: ")

        print(x(x2, bin))
    case "4":
        x2 = input("Введите число: ")

        print(x(x2, hex))
    case _:
        print("Ошибка!\nВведите вариант от 1 до 4")
