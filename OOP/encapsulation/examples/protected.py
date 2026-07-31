class Person:
    def __init__(self,name,salary):
        self.name = name
        self._salary = salary

P1 = Person("Harshal",200000)
print(P1.name)
print(P1._salary)