class Asker:
    @staticmethod
    def askall(lst):
        for i in lst:
            i.report()


class Sender:
    flag = True

    @classmethod
    def report(cls):
        if cls.flag:
            print('Greetings!')
            cls.flag = False
        else:
            print('Get away!')

Asker.askall([Sender() for i in range(3)] * 2)
