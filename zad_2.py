# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 15:58:47 2022

@author: BBrzek
"""
class Library:
    def __init__(self, city, street, zip_code, open_hours: str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone
    def __str__(self) -> str:
        return f"{self.city},{self.street}, {self.zip_code}, {self.open_hours}, {self.phone}"
    

class Employee():
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone
    def __str__(self) -> str:
        return f"{self.first_name},{self.last_name}, {self.hire_date}, {self.birth_date}, {self.city}, {self.street}, {self.zip_code}, {self.phone} "


class Student:
    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = marks
        
    def is_passed(self) -> bool:
        return sum(self.marks)/len(self.marks) > 50
    def __str__(self)-> str:
        return f"{self.name}, {self.marks}"
class Book(Library):
    def __init__(self, library: Library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages
    def __str__(self) -> str:
        return f"{self.library.__str__()}, {self.publication_date}, {self.author_name}, {self.author_surname}, {self.number_of_pages}"
class Order(Employee, Student, Book):
    def __init__(self, employee: Employee, student: Student,books: Book, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date
        
    def __str__(self) -> str:
        return f"{self.employee.__str__()}, {self.student.__str__()}, {self.books.__str__()},{self.order_date}"

lib1 = Library('Katowice','Kociuszki','44-444','16-20','511222333')
lib2 = Library('Warszawa','Markowska','22-222','8-12','111222888')

book1 = Book(lib1, '06-06-1900', 'Mark', 'Autorrrus', '200')
book2 = Book(lib1, '03-01-1800', 'Tom', 'Walor', '365')
book3 = Book(lib1, '05-06-2000', 'John', 'Partul', '777')
book4 = Book(lib2, '12-12-2012', 'Janus', 'Bolel', '999')
book5 = Book(lib2, '31-08-2008', 'Pyrko', 'Bobo', '100')

emp1 = Employee('Jan', 'Kowalski','06-06-1900', '06-06-1860', 'Katowice','Kociuszki','44-444','511222333' )
emp2 = Employee('Michal', 'Nowak','06-06-2000', '06-06-2010', 'Katowice','Kociuszki','44-444','511222333' )
emp3 = Employee('Tomasz', 'Pyrski','06-06-2010', '06-06-2000', 'Warszawa','Kociuszki','44-444','511222333' )

s1_name = 'Mark'
s1_marks = [60,40,50,70]
s1 = Student(s1_name, s1_marks)

s2_name = 'Tom'
s2_marks = [30,40,40,70]
s2 = Student(s2_name, s2_marks)


s3_name = 'John'
s3_marks = [30,60,40,80]
s3 = Student(s3_name, s3_marks)

order1 = Order(emp1, s3, book1, '22-03-2022')
order2 = Order(emp2, s2, book5, '22-03-2022')

print(order1.__str__())
print(order2.__str__())