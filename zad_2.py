# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 15:45:27 2022

@author: BBrzek
"""


def fc_imiona(listaImion):
    for i in range(len(listaImion)):
        print(listaImion[i])


def fc_liczby_a(listaLiczb):
    liczby = []
    for liczba in listaLiczb:
        liczby.append(liczba * 2)
    return liczby


def fc_liczby_b(listaLiczb):
    liczby = [liczby * 2 for liczby in listaLiczb]
    return liczby


def fc_liczby_c(listaLiczb):
    for i in range(len(listaLiczb)):
        if listaLiczb[i] % 2 == 0:
            print(listaLiczb[i])


def fc_liczby_d(listaLiczb):
    for i in range(1, len(listaLiczb), 2):
        print(listaLiczb[i])


imiona = ["Marek", "Paweł", "Jan", "Mirosław", "Lech"]
print('Zadanie 2.a')
fc_imiona(imiona)
l_liczby = [1, 2, 3, 4, 5]
print('Zadanie 2.b1')
print(fc_liczby_a(l_liczby))
print('Zadanie 2.b2')
print(fc_liczby_b(l_liczby))
lista_liczb_10 = [3, 2, 3, 2, 4, 6, 2, 8, 8, 10]
print('Zadanie 2.c')
fc_liczby_c(lista_liczb_10)
print('Zadanie 2.d')
fc_liczby_d(lista_liczb_10)
