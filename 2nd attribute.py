class Customer:
    def set_name(self,new_name):
        self.name = new_name

    def identity(self):
        print("Your name is " + self.name)

cust = Customer()
cust.set_name("Akoto Boadi")
cust.identity()
print(cust.name)