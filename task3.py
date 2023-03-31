import math
def equation(a, b ,c):
    try:
        discr = b ** 2 - 4 * a * c
        print("Дискриминант D = %.2f" % discr)
        if discr > 0:
            x1 = (-b + math.sqrt(discr)) / (2 * a)
            x2 = (-b - math.sqrt(discr)) / (2 * a)
            return f"x1 = %.2f \nx2 = %.2f" % (x1, x2)
        elif discr == 0:
            x = -b / (2 * a)
            return f"x = %.2f" % x
        else:
            return f"Корней нет"
    except:
        return f"Введите верные переменные"
print(equation(1, 2, 3))