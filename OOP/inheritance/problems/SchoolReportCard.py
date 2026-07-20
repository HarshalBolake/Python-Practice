class Person:
    def __init__(self,name):
        self.name = name
        self.marks = None
        self.grade = None
        self.average = None

class Student(Person):    
    def calculate_grade(self,marks):
        self.marks = marks
        if(marks > 90):
            self.grade = "A"
        elif(marks > 80):
            self.grade = "B"
        elif(marks > 70):
            self.grade = "C"
        else:
            self.grade = "D"
    
        print(f"Marks = {marks} & Grade = {self.grade}")
        
class GraduateStudent(Student):
    def Average_marks(self,project_marks):
        self.average = self.marks + (project_marks / 2)

        print(f"Average Marks: {self.average}")

    
GS1 = GraduateStudent("Harshal")
GS1.calculate_grade(88)
GS1.Average_marks(56)