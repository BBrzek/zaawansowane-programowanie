# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 15:45:56 2022

@author: BBrzek
"""

class Student:
    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = marks
        
    def is_passed(self) -> bool:
        return sum(self.marks)/len(self.marks) > 50
        


s1_name = 'Mark'
s1_marks = [60,40,50,70]
s1 = Student(s1_name, s1_marks)
print('Student Mark: ' + str(s1.is_passed()))
s2_name = 'Tom'
s2_marks = [30,40,40,70]
s2 = Student(s2_name, s2_marks)
print('Student Tom: ' + str(s2.is_passed()))