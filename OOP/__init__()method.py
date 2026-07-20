class Person:
    def __init__(self,name):
        self.name = name


    def greet(self):
        return "Hello "+self.name

    def welcome(self):
        message = self.greet()
        print(message + " welcome to python")

P1 = Person("Harshal")
P1.welcome()



