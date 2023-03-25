from typing import Union


# 102936456214652135727561205, 92057275512051510293645621465513572755120529364562146275512
# 72750120615, 77776710012
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
        var1 = input("Введите первое число: ")
        var2 = input("Введите второе число: ")
        result = str(int(var1) + int(var2))

        print(x(result, int))

    case "2":
        var1 = input("Введите первое число: ")
        var2 = input("Введите второе число: ")
        result = str(int(var1) + int(var2))

        print(x(result, oct))
    case "3":
        var1 = input("Введите первое число: ")
        var2 = input("Введите второе число: ")
        result = str(int(var1) + int(var2))

        print(x(result, bin))
    case "4":
        var1 = input("Введите первое число: ")
        var2 = input("Введите второе число: ")
        result = str(int(var1) + int(var2))

        print(x(result, hex))
    case _:
        print("Ошибка!\nВведите вариант от 1 до 4")
