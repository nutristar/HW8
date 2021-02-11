"""Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
 Проверьте его работу на данных, вводимых пользователем.
  При вводе пользователем нуля в качестве делителя программа должна
корректно обработать эту ситуацию и не завершиться с ошибкой."""

class Message(Exception):
    def __init__(self,message):
        self.message=message
        #return self.message


in_data = input("на что поделим число 100?:")
try:
    in_data=int(in_data)
    if in_data==0:
        raise Message("на ноль делить нельзя!!!")
except ValueError:
    print("Error type of value!")
except Message as err:
    print(err)
else:

    print(100/int(in_data))