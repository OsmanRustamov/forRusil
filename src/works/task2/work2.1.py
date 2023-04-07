def conversion_to_another_number_system(num_str: str, number_system_type):
    numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    match number_system_type:
        case "1":
            if num_str.isdigit():
                return num_str
            return "Ошибка!\nИмеется буква"
        case "2":
            if num_str.isdigit():
                for number in num_str:
                    if number in numbers_list[8::]:
                        return "Несоответсвия числа заданной системе счисления"
                return num_str
            return "Ошибка!\nИмеется буква"

        case "3":
            if num_str.isdigit():
                for number in num_str:
                    if number in numbers_list[2::]:
                        return "Несоответсвия числа заданной системе счисления"
                return num_str
            return "Ошибка!\nИмеется буква"
        case "4":
            for number in num_str:
                if number not in numbers_list:
                    return "Ошибка!\nИмеется буква"
            return num_str


if __name__ == '__main__':
    user_choice = input(
        "Выберите систему счисления:\n1) Десятичная (10-ичная)\n2) Восьмиричная (8-ичная)\n3) Двоичная (2-ичная)\n4) Шестнадцатиричная (16-ичная)\nВведите номер выбранной опции: ")

    match user_choice:
        case "1":
            user_input = input("Введите число: ")

            print(conversion_to_another_number_system(user_input, "1"))
        case "2":
            user_input = input("Введите число: ")

            print(conversion_to_another_number_system(user_input, "2"))
        case "3":
            user_input = input("Введите число: ")

            print(conversion_to_another_number_system(user_input, "3"))
        case "4":
            user_input = input("Введите число: ")

            print(conversion_to_another_number_system(user_input, "4"))
        case _:
            print("Ошибка!\nВведите вариант от 1 до 4")
