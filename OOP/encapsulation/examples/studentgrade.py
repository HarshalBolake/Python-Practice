class Student:
    def __init__(self,name):
        self.name = name
        self.__grade = 0

    def set_grade(self,grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Grade must be between 0 and 100")

    def get_grade(self):
        return self.__grade
    
    def get_status(self):
        if self.__grade >= 60:
            return "Passed"
        else:
            return "Failed"
        
S1 = Student("Harshal")
S1.set_grade(85)
print(S1.get_grade())
print(S1.get_status())