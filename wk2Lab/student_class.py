# class Student: # this is the original version
#     def __init__(self, name, student_id, gpa):
#         self.name = name
#         self.student_id = student_id
#         self.gpa = gpa

#     def __str__(self):
#         return f'Name: {self.name}, id: {self.student_id}, gpa: {self.gpa}'

# def main():
#     sierra = Student('Sierra', '123456', 3.8) #creating Student objects
#     nicole = Student('Nicole', '234567', 3.9)
#     acadia = Student('Acadia', '345678', 2.3)
    
#     print(sierra.gpa)
#     sierra.gpa = 3.7
#     print(sierra.gpa)
# main()

#below using dataclass
from dataclasses import dataclass #using dataclass makes your code much simpler

@dataclass  #when using @dataclass decorator, don't need self.name, __init__() or __str__() method; they are automatic
class Student:
    name: str  #when using dataclass, need to tell python the data types: str, int, float
    student_id: int
    gpa: float

def main():
    sierra = Student('Sierra', 123456, 3.8) #creating Student objects
    nicole = Student('Nicole', 234567, 3.9)
    acadia = Student('Acadia', 345678, 2.3)
    
    print(sierra.gpa)
    sierra.gpa = 3.7 #changing the gpa
    print(sierra.gpa) #shows new gpa
    print(acadia.student_id)
    print(nicole) #prints whole object using __str__()


main()