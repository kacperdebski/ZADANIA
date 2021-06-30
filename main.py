import math

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
        if lista.ilosc(liczba) > 1:
            return liczba
