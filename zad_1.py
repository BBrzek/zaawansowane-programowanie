# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 16:44:05 2022

@author: BBrzek
"""
def fc_przywitanie(name: str, surname: str) -> str:
    return f'Czesc {name} {surname}!'

wynik = fc_przywitanie('Jacek', 'Placek')
print(wynik)
