# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 16:58:05 2022

@author: BBrzek
"""
def fc_sumy(a: int, b: int, c: int) -> bool:
    if a+b >= c:
        return True
    else:
        return False
    

print(fc_sumy(1,2,4))
