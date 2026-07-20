class Person:
    def introduce(self,name,age):
        print(f"hello my name is {name} and i am {age} year old.")


class Student(Person):
    def study(self):
        print(f"currently i am studying in NTU")


class Professor(Person):
    def teach(self):
        print(f"my professor name is neil")

class ResearchAssistant(Student,Professor):
    def research(self):
        print(f"my research assistant is also neil")

RA1 = ResearchAssistant()
RA1.introduce("Harshal",22)
RA1.study()
RA1.teach()
RA1.research()
