from math import pow, pi
from typing import Union, Any


def multiplicar(x, y):
    multi = x * y
    return multi


def numPar(valor1):
    if valor1 % 2 == 0:
        par = True
        return par
    else:
        par = False
        return par


def primo(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True


def calcula_volume(raio):
    return (3 / 4) * pi * pow(raio, 3)


def segundos(h, m, s):
    totalSegundos: Union[int, Any] = ((h * 60) * 60) + (m * 60) + s
    return totalSegundos
