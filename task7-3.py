'''
3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы
перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление
(__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться округление значения
до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих
двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод
 позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
'''


class BodyCell:

    def __init__(self, count_cells):
        self.count_cells = count_cells

    def __add__(self, other):
        return self.count_cells + other.count_cells

    def __sub__(self, other):
        if self.count_cells > other.count_cells:
            return self.count_cells - other.count_cells
        else:
            return 'Вычитание клеток невозможно, т.к. в первом объекте клеток меньше, чем во втором'

    def __mul__(self, other):
        return self.count_cells * other.count_cells

    def __truediv__(self, other):
        return self.count_cells // other.count_cells

    def make_order(self, cells_in_a_row):
        result_string = str()
        if self.count_cells // cells_in_a_row == 0:
            for i in range(self.count_cells):
                result_string += '*'
        elif self.count_cells // cells_in_a_row >= 1:
            for i in range(self.count_cells // cells_in_a_row):
                for k in range(cells_in_a_row):
                    result_string += '*'
                result_string += '/n'
            if self.count_cells % cells_in_a_row > 0:
                for k in range(self.count_cells % cells_in_a_row):
                    result_string += '*'
        if result_string[-1] == 'n':
            return result_string[:-2]
        else:
            return result_string


cell1 = BodyCell(21)
cell2 = BodyCell(6)
print(cell1 + cell2)
print(cell1 - cell2)
print(cell1 * cell2)
print(cell1 / cell2)
print(cell1.make_order(5))
