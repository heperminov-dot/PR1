import math  # підключення бібліотеки

def task_integer13():
    """Integer13:
    Дано тризначне число.
    Закреслити першу зліва цифру і приписати її справа.
    Вивести отримане число.
    """
    try: # виконання коду
        n = int(input("Введіть тризначне число n = "))
        if n < 100 or n > 999:
            raise ValueError("Число повинно бути тризначним!")
    except ValueError as e: # якщо є помилка
        print("Помилка:", e)
    else:  # якщо немає помилки
        first_digit = n // 100       # перша цифра
        last_two = n % 100           # останні дві цифри
        result = last_two * 10 + first_digit
        print("Отримане число:", result)


def task_math41():
    """Завдання 2:
    Математичний вираз
    """
    try:
        x = float(input("Введіть x = "))
    except ValueError:
        print("Помилка: x має бути числом!")
    else:
        try:
            numerator = pow(x, 1/4) + math.sqrt(abs(x**3)) # чисельник лівого виразу
            denominator = math.log2((math.sin(abs(x))**2)**2) # знаменник лівого виразу
            term2 = (2 * math.pi * abs(math.tan(x))) / 12 # правий вираз
            y = numerator / denominator + term2 # увесь вираз
        except ValueError: # помилка при введені нуля
            print("Помилка обчислення: перевірте область визначення функцій!")
        else:
            print("Результат y =", y)


def task_boolean15():
    """Boolean15:
    Дано A, B, C.
    Перевірити істинність висловлювання:
    «Рівно два з чисел A, B, C є позитивними».
    """
    try:
        A = int(input("A = "))
        B = int(input("B = "))
        C = int(input("C = "))
    except ValueError:
        print("Помилка: всі значення повинні бути цілими!")
    else:
        positives = (A > 0) + (B > 0) + (C > 0)
        result = positives == 2
        print("Рівно два з чисел позитивні:", result)


# --- виклики функцій по порядку ---
task_integer13()
task_math41()
task_boolean15()
