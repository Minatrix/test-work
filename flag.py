n = int(input("Enter even integer number:"))

class ArgumentError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def flag(n):
    if n % 2 == 0:
        # Верхняя граница
        s1 = "#" * (3 * n + 2)
        # Заполнение флага до центрального рисунка
        cycle1 = int(round(n / 2))
        s2 = ""
        while cycle1 != 0:
            s2 = s2 + "#" + " " * (3 * n) + "#" + '\n'
            cycle1 = cycle1 - 1
        # Первая строка центрального рисунка
        s2 = s2 + "#" + " " * int(1.5 * n - 1) + "**" + " " * int(1.5 * n - 1) + "#"
        # Строки центрального рисунка увеличение
        cycle2 = (n - 2) / 2
        s3 = ""
        max_o = n - 2
        dop_o = 2
        while cycle2 != 0:
            s3 = s3 + "#" + " " * int(1.5 * n - 1 - dop_o / 2) + "*" + "o" * dop_o + "*" + " " * int(
                1.5 * n - 1 - dop_o / 2) + "#" + '\n'
            cycle2 = cycle2 - 1
            dop_o = dop_o + 2
        # Строки центрального рисунка уменьшение
        cycle2 = (n - 2) / 2
        dop_o = dop_o - 2
        while cycle2 != 0:
            s3 = s3 + "#" + " " * int(1.5 * n - 1 - dop_o / 2) + "*" + "o" * dop_o + "*" + " " * int(
                1.5 * n - 1 - dop_o / 2) + "#" + '\n'
            cycle2 = cycle2 - 1
            dop_o = dop_o - 2
        # Последняя строка центрального рисунка
        s3 = s3 + "#" + " " * int(1.5 * n - 1) + "**" + " " * int(1.5 * n - 1) + "#"
        # Заполнение флага после центрального рисунка
        cycle3 = int(round(n / 2))
        s4 = ""
        while cycle3 != 0:
            s4 = s4 + "#" + " " * (3 * n) + "#" + '\n'
            cycle3 = cycle3 - 1
        # Нижняя граница
        s4 = s4 + "#" * (3 * n + 2)

        s_print = s1 + '\n' + s2 + '\n' + s3 + '\n' + s4
        print(s_print)
    else:
        raise ArgumentError('Failed')

flag(n)