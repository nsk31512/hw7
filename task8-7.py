'''
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
'''


class ComplexNumber:

    def __init__(self, a, b):
        """a и b - вещественные числа комплексного числа (a+bi)"""
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a}+{self.b}i'

    def __add__(self, other):
        return f'{(self.a + other.a)}+{(self.b + other.b)}i'

    def __sub__(self, other):
        return f'{(self.a - other.a)}-{(self.b - other.b)}i'

    def __mul__(self, other):
        return f'{(self.a * other.a - self.b * other.b)}+{(self.b * other.a + self.a * other.b)}i'

    def __truediv__(self, other):
        nominator1 = self.a * other.a + self.b * other.b
        denominator = other.a**2 + other.b**2
        nominator2 = self.b * other.a - self.a * other.b
        return f'{nominator1/denominator:.2f}+{nominator2/denominator:.2f}i'


complex1 = ComplexNumber(5, 6)
complex2 = ComplexNumber(10, 11)
print(complex1)
print(complex2)
print(complex1 + complex2)
print(complex2 - complex1)
print(complex1 * complex2)
print(complex1 / complex2)
