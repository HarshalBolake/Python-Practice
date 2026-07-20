class User:
    def __init__(self,name):
        self.name = name

    def user_login(self):
        print("User Login")
    
    def user_logout(self):
        print("User Logout")

class Customer(User):
    def place_order(self):
       print(f"{self.name} placed an order.")
    
class DeliveryPartner(User):
    def deliver_order(self):
        print(f"{self.name} delivered the order.")

class Order:
    def __init__(self,order_id,amount):
        self.order_id = order_id

        if amount < 0 :
            return ValueError("Order amount cannot be negative.")

        self.amount = amount
        self.discount = 0

    def apply_discount(self,discount):
        if discount < 0:
            print("Discount cannot be negative.")
        if discount > self.amount:
            print("Discount cannot be grater than the order amount.")
            return
            
        self.discount = discount

    def final_amount(self):
        return self.amount - self.discount
        
    def order_summary(self):
        print("\n------Order Summary------")
        print(f"Order Id: {self.order_id}")
        print(f"Order Amount: {self.amount}")
        print(f"Discount: {self.discount}")
        print(f"Final amount: {self.final_amount()}")
        print("------------------------------")

        
customer = Customer("Harshal")
customer.user_login()
customer.place_order()

order = Order(101,1500)
order.apply_discount(200)
order.order_summary()

partner = DeliveryPartner("Tom")
partner.user_login()
partner.user_logout()

customer.user_logout()