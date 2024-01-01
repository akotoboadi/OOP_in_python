# creating attributes in python 
class Customer:
    def set_name(self,new_name):
        self.name = new_name

cust = Customer()
cust.set_name("Akoto Boadi")
print(cust.name)