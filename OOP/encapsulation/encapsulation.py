
#Example 1
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age

#     def get_age(self):
#         return self.__age

# P1 = Person("Harshal",22)
# print("name: ",P1.name)
# # print("age: ",P1.age)
# print(P1.get_age())


#Example 2
class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age
    
    def get_age(self):
        return self.__age
    
    def set_age(self,age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")

P1 = Person("Harshal",18)
print(P1.get_age())

P1.set_age(22)
print(P1.get_age())

