# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 17:04:16 2022

@author: BBrzek
"""
def fc_listy(a: list, b: list) -> list:
    lista = a+b
    return [element ** 3 for element in list(set(lista))]
    
    
print(fc_listy([1,2,3,4],[3,4,5,6]))
    
