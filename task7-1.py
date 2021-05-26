'''
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
первым элементом первой строки второй матрицы и т.д.
'''


class Matrix:

    def __init__(self, args):
        self.args = args

    def __str__(self):
        line_str = str()
        for item in self.args:
            line_str += str(item) + '\n'
        return line_str

    def __add__(self, other):
        if len(self.args) < len(other.args):
            for i in range(len(self.args)):
                add_string = [0] * len(self.args[i])
            self.args.append(add_string)
        elif len(self.args) > len(other.args):
            for i in range(len(other.args)):
                add_string = [0] * len(other.args[i])
            other.args.append(add_string)

        for i in range(len(self.args)):
            if len(self.args[i]) < len(other.args[i]):
                for j in range(len(other.args[i])-len(self.args[i])):
                    self.args[i].append(0)
            elif len(self.args[i]) > len(other.args[i]):
                for j in range(len(self.args[i]) - len(other.args[i])):
                    other.args[i].append(0)

        result_list = list()
        for i in range(len(self.args)):
            sum_in_row = list()
            for j in range(len(self.args[i])):
                sum_in_row.append(self.args[i][j] + other.args[i][j])
            result_list.append(sum_in_row)
        return Matrix(result_list)


list_of_lists = [[1, 2, 5], [4, 5, 6], [7, 8, 9, 11], [7, 8, 9, 11, 20]]
list_of_lists2 = [[1, 2, 3], [4, 5], [7], [1, 2, 3]]
matr = Matrix(list_of_lists)
print(matr)
matr2 = Matrix(list_of_lists2)
sum_of_matrix = matr + matr2
print(sum_of_matrix)
