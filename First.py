""" Реализовать класс «Дата», функция-конструктор которого
 должна принимать дату в виде строки формата «день-месяц-год».
 В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
  должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
   Второй, с декоратором @staticmethod, должен проводить валидацию числа,
    месяца и года (например, месяц — от 1 до 12).
 Проверить работу полученной структуры на реальных данных."""
dmy = "15-01-2028"


class Data:

    def __init__(self, dmy):
        self.dmy = dmy

    @classmethod
    def digitalisator(cls, dmy):
        num = []
        for i in dmy.split('-'):
            num.append(int(i))
        return Data.validation(num)


    @staticmethod
    def validation(num):

        if num[0] > 31 or num[0] <= 0:
            return ("input correct day")
        elif num[1] <= 0 or num[1] > 12:
            return ("input correct month")
        elif num[2] > 2021:
            return ("input correct Year")
        else:
            return num


print(Data.digitalisator(dmy))
