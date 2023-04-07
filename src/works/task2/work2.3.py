# 102936456214652135727561205, 92057275512051510293645621465513572755120529364562146275512
# 72750120615, 77776710012
def compare_numbers(num1: str, num2: str) -> str:
    if not num1.isdigit() or not num2.isdigit():
        return "Ошибка!\nИмеется буква"

    if int(num1) > int(num2):
        return "Первое число больше второго"
    elif int(num1) < int(num2):
        return "Первое число меньше второго"
    else:
        return "Числа равны"


if __name__ == '__main__':
    var1 = input("Введите первое число: ").strip()
    var2 = input("Введите второе число: ").strip()

    print(compare_numbers(var1, var2))
