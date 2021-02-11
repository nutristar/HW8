class Message(Exception):
    def __init__(self,message):
        self.message=message


my_list=[]
#@staticmethod
class Repieter:
    def tryexepter():
        try:
            while True:
                i = input("введи ЧИСЛО,   для выхода введите stop")
                if i=="stop":
                    print (my_list)
                    break
                elif i.isdigit():
                    my_list.append(i)
                else:
                    raise Message("вводите только числа")
        except Message as err:
            print(err)
            return Repieter.tryexepter()

one=Repieter.tryexepter()
one