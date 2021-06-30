import math
#ZADANIE 1
def z1a(liczba: int) -> bool:
    return liczba % 3 == 0
def z1b(liczba: int) -> bool:
    return int(math.sqrt(liczba)) ** 2 == liczba
#ZADANIE 2
def z2a(lista: list[int]) -> int:
    najmniejsza = None
    najwieksza = None
    for i in lista:
        if najmniejsza == None or najmniejsza > i:
            najmniejsza = i
        if najwieksza == None or najwieksza < i:
            najwieksza = i
        return(najwieksza - najmniejsza)

def z2b(lista: list[int]) -> int:
    for liczba in range(min(lista),max(lista)):
        if liczba not in lista:
            return liczba

def z2c(lista: list[int]) -> list[int]:
    rlist = []
    for liczba in range(min(lista), max(lista)):
        if liczba not in lista:
            rlist.append(liczba)
        return rlist

def z2d(lista: list[int]) -> int:
    for liczba in lista:
        if lista.count(liczba) > 1:
            return liczba

def z2e(lista: list[int]) -> set[int]:
    rlist = set()
    for liczba in lista:
        if lista.count(liczba) > 1:
            rlist.add(liczba)
    return rlist
#ZADANIE 3
from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def A(self):
        pass

class Kwadrat(Figura):
    def __init__(self, bok1):
        self.bok1 = bok1

    def oblicz_pole(self):
        return self.bok1 ** 2

class Prostokat(Kwadrat):
    def __init__(self, bok1, bok2):
        super().__init__(bok1)
        self.bok2 = bok2

    def oblicz_pole(self):
        return self.bok1 * self.bok2
