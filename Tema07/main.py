from abc import ABC, abstractmethod


class FormaGeometrica(ABC):
    pi = 3.14

    @abstractmethod
    def aria(self):
        pass

    def descrie(self):
        print("Cel mai probabil am colturi")


class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.__latura = latura

    @property
    def get_latura(self):
        return self.__latura

    def set_latura(self, new_latura):
        self.__latura = new_latura

    def delete_latura(self):
        del self.__latura

    def aria(self):
        return self.__latura ** 2


class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.__raza = raza

    @property
    def get_raza(self):
        return self.__raza

    def set_raza(self, new_raza):
        self.__raza = new_raza

    def delete_raza(self):
        del self.__raza

    def aria(self):
        return self.pi * self.__raza ** 2

    def descrie(self):
        print("Eu nu am colturi")


patrat1 = Patrat(5)
patrat1.descrie()
print("Latura patratului este:", patrat1.get_latura)
print("Aria patratului este:", patrat1.aria())
patrat1.set_latura(8)
print("Dupa apelarea metodei 'set', latura patratului este:", patrat1.get_latura)
print("Aria patratului devine:", patrat1.aria())
patrat1.delete_latura()
# patrat1.get_latura  #  <-- if we do this, we'll get an AttributeError, because after delete, object has no attribute
print("------------------------------------------------------")
cerc1 = Cerc(3)
cerc1.descrie()
print("Raza cercului este:", cerc1.get_raza)
print("Aria cercului este:", cerc1.aria())
cerc1.set_raza(5)
print("Dupa apelarea metodei 'set', raza cercului este:", cerc1.get_raza)
print("Aria cercului devine:", cerc1.aria())
cerc1.delete_raza()
# cerc1.get_raza  #  <-- if we do this, we'll get an AttributeError, because after delete, object has no attribute
