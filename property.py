from string import ascii_letters

class Person:
    rus = "абвгдеёжзийклмнопрстуфхцчшщыьъэюя-"
    rus_UPPER = rus.upper()

    def __int__(self, fio, old, ps, weight):
        self.veri_fio(fio)
        self.veri_old(old)
        self.veri_ps(ps)
        self.veri_weight(weight)

        self.__fio = fio.split()
        self.__old = old
        self.__passport = ps
        self.__weight = weight

    @classmethod
    def veri_fio(cls, fio):
        if type(fio) != str:
            raise TypeError('ФИО должно быть строкой')
        f = fio.split()
        if len(f) != 3:
            raise TypeError('Неверный формат ФИО')
        let = ascii_letters + cls.rus + cls.rus_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError('В ФИО должен быть хоть один символ')
            if len(s.strip(let)) != 0:
                raise TypeError('В ФИО должны быть только буквы и дефис')

    @classmethod
    def veri_old(cls, old):
        if type(old) != int or old < 18 or old > 90:
            raise TypeError('Не подходит возраст')

    @classmethod
    def veri_weight(cls, w):
        if type(w) != float or w < 40 or w > 200:
            raise TypeError('Не подходит вес')

    @classmethod
    def veri_ps(cls, ps):
        if type(ps) != str:
            raise TypeError('Паспорт должен быть строкой')
        s = ps.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError('Неверный формат паспорта')
        for i in s:
            if not i.isdigit():
                raise TypeError('Паспорт должен состоять из цифр')
    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, fio):
        self.veri_fio(fio)
        self.__fio = fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.veri_old(old)
        self.__old = old

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, w):
        self.veri_weight(w)
        self.__weight = w

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, ps):
        self.veri_ps(ps)
        self.__passport = ps

p = Person()
p.old = 38
p.passport = '1234 567890'
p.weight = 77.5
p.fio = 'Рожков Сергей Николаевич'

print(p.__dict__)
