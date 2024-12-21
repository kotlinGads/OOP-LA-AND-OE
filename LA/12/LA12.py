print ("LA #12")

class Toy():
    def __init__(self,name,price):
        self.name = name
        self.price = price
    
    def describeToy(self):
        print(f'Name:{self.name}, Price:{self.price}')
  
class Car(Toy):
    def __init__(self,name,price):
        super().__init__(name,price)
        
letsgo = Car("broom broom ni aron", "50")
letsgo.describeToy()