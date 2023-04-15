from datetime import date

"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных."""


class Date:
    @classmethod
    def extraction(cls, string):
        lst = list(map(int, string.split('-')))
        return lst

    @staticmethod
    def validate(lst):
        number = lst[0]
        month = lst[1]
        year = lst[2]
        try:
            date(year, month, number)
            return "Дата корректна"
        except ValueError:
            return "Некорректная дата"

    def __init__(self, string):
        self.res = self.validate(self.extraction(string))


"""
2. Создайте собственный класс-исключени, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных, 
вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не 
завершиться с ошибкой."""


class DivisionZero:
    @staticmethod
    def calculation(x, y):
        try:
            return x / y
        except ZeroDivisionError:
            return 'Division by zero'

    def __init__(self, x, y):
        self.x = x
        self.y = y


"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо только
числами. Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
скрипта, введя, например, команду «stop». При этом скрипт завершается, сформированный список с числами выводится на 
кран.
Подсказка: для этого задания примем, что пользователь может вводить только числа и строки. Во время ввода пользователем 
очередного элемента необходимо реализовать проверку типа элемента. Вносить его в список, только если введено число. 
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение. 
При этом работа скрипта не должна завершаться."""


class Numbers:
    numbers = []

    def __init__(self, x):
        self.x = x

    @classmethod
    def validate(cls, x):
        if x.isdigit():
            cls.numbers.append(int(x))
            return cls.numbers
        else:
            print('Enter the number!')

    @classmethod
    def result(cls):
        return cls.numbers


"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», 
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры, 
уникальные для каждого типа оргтехники.
                                                    * * *

class WarehouseOfOfficeEquipment:
    def __init__(self, address, telephone):
        self.address = address
        self.telephone = telephone


class OfficeEquipment:
    def __init__(self, name, manufacturer, model, price):
        self.name = name
        self.manufacturer = manufacturer
        self.model = model
        self.price = price


class Printer(OfficeEquipment):
    def __init__(self, name, manufacturer, model, price, kind):
        super().__init__(name, manufacturer, model, price)
        self.kind = kind


class Scanner(OfficeEquipment):
    def __init__(self, name, manufacturer, model, price, sensor):
        super().__init__(name, manufacturer, model, price)
        self.sensor = sensor


class Xerox(OfficeEquipment):
    def __init__(self, name, manufacturer, model, price, dpi=600):
        super().__init__(name, manufacturer, model, price)
        self.dpi = dpi

=======================================================================================================================
                                                    
5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу 
в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру (например, словарь).
                                                    * * *

class WarehouseOfOfficeEquipment:
    product = {}

    @classmethod
    def acceptance_of_goods(cls, name, manufacturer, model, quantity):
        cls.product[(name, manufacturer, model,)] = cls.product.get((name, manufacturer, model,), 0) + quantity

    @classmethod
    def transfer_of_goods(cls, name, manufacturer, model, quantity):
        cls.product[(name, manufacturer, model,)] -= quantity


class OfficeEquipment(WarehouseOfOfficeEquipment):
    def __init__(self, name, manufacturer, model, quantity):
        self.name = name
        self.manufacturer = manufacturer
        self.model = model
        self.price = quantity


class Printer(OfficeEquipment):
    def __init__(self, name, manufacturer, model, quantity, kind):
        super().__init__(name, manufacturer, model, quantity)
        self.kind = kind


class Scanner(OfficeEquipment):
    def __init__(self, name, manufacturer, model, quantity, sensor):
        super().__init__(name, manufacturer, model, quantity)
        self.sensor = sensor


class Xerox(OfficeEquipment):
    def __init__(self, name, manufacturer, model, quantity, dpi=600):
        super().__init__(name, manufacturer, model, quantity)
        self.dpi = dpi

=======================================================================================================================

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для 
указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных."""


class WarehouseOfOfficeEquipment:
    product = {}

    @classmethod
    def acceptance_of_goods(cls, name, manufacturer, model, quantity):
        if quantity.isdigit():
            cls.product[(name, manufacturer, model,)] = cls.product.get((name, manufacturer, model,), 0) + int(quantity)
        else:
            print('The number of units must be a number!')

    @classmethod
    def transfer_of_goods(cls, name, manufacturer, model, quantity):
        if quantity.isdigit():
            cls.product[(name, manufacturer, model,)] -= int(quantity)
        else:
            print('The number of units must be a number!')


class OfficeEquipment(WarehouseOfOfficeEquipment):
    def __init__(self, name, manufacturer, model, quantity):
        self.name = name
        self.manufacturer = manufacturer
        self.model = model
        self.price = quantity


class Printer(OfficeEquipment):
    def __init__(self, name, manufacturer, model, quantity, kind):
        super().__init__(name, manufacturer, model, quantity)
        self.kind = kind


class Scanner(OfficeEquipment):
    def __init__(self, name, manufacturer, model, quantity, sensor):
        super().__init__(name, manufacturer, model, quantity)
        self.sensor = sensor


class Xerox(OfficeEquipment):
    def __init__(self, name, manufacturer, model, quantity, dpi=600):
        super().__init__(name, manufacturer, model, quantity)
        self.dpi = dpi


"""7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». 
Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта. 
Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров. 
Проверьте корректность полученного результата."""


class Complex:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "{0} + {1}j".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Complex(x, y)

    def __mul__(self, other):
        x = self.x * other.x - self.y * other.y
        y = self.x * other.y + self.y * other.x
        return Complex(x, y)


if __name__ == '__main__':
    # 1. --------------------------------------------------------------------------------------------------------------
    # print(Date('12-12-2022').res)
    # print(Date('29-02-2023').res)
    # print(Date('12-1-22').res)
    # print(Date('32-11-1978').res)

    # 2. --------------------------------------------------------------------------------------------------------------
    # print()
    # print(DivisionZero.calculation(3, 2))
    # print(DivisionZero.calculation(3, 0))

    # 3. --------------------------------------------------------------------------------------------------------------
    # number = input()
    # res = Numbers(number)
    # while number != 'stop':
    #     res.validate(number)
    #     number = input()
    # print(*res.result())

    # 4-6. _-----------------------------------------------------------------------------------------------------------

    # a = WarehouseOfOfficeEquipment()
    # a.acceptance_of_goods('printer', 'asus', 'x86', '12')
    # a.acceptance_of_goods('scanner', 'gigabyte', 'x64', '2')
    # a.acceptance_of_goods('xerox', 'mts', 'x86', '3')
    # b = Xerox('xerox', 'mts', 'x86', '6')
    # b.acceptance_of_goods('xerox', 'mts', 'x86', '6')
    # print(a.product)
    # print(b.product)
    # print(b.dpi)
    # print(b.name)
    # b.transfer_of_goods('xerox', 'mts', 'x86', '8g')
    # a.acceptance_of_goods('xerox', 'mts', 'x86', '3f')

    # 7. --------------------------------------------------------------------------------------------------------------
    a = Complex(1, 2)
    print(a.__dict__)
    b = Complex(4, 5)
    print(b.__dict__)
    print(a + b)
    print(a * b)
