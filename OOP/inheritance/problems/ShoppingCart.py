class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    
    def display(self):
        print(f"Product name: {self.name}")
        print(f"Product price: {self.price}")

class Electronics(Product):
    def Warranty(self):
        print("2 years warranty")

class Clothing(Product):
    def Size(self):
        print("Size: L")
    
class Food(Product):
    def ExpiryDate(self):
        print("Expiry Date: 28 july")

E1 = Electronics("Tablet",30000)
E1.display()
E1.Warranty()

C1 = Clothing("T-shirt",1000)
C1.display()
C1.Size()

F1 = Food("Chicken",250)
F1.display()
F1.ExpiryDate()