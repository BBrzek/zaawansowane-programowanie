# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 16:51:03 2022

@author: student
"""
def fc_czyParzysta(liczba: int) -> bool:
    if liczba%2==0:
        return True
    else:
        return False

wynik = fc_czyParzysta(3)
if wynik:
    print('Liczba parzysta')
else:
    print('Liczba nieparzysta')