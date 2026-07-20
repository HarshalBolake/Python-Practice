class Human:
    species = "Human"

    def __init__(self,name):
        self.name = name
    
H1 = Human("Harshal")
H2 = Human("dog")

print(H1.name)
print(H1.species)

Human.species = "Animal" #change properties

print(H2.name)
print(H2.species)

H1.age = 22             #adding properties
H2.age = 8

print(H1.age)