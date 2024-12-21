print("LA16")

class Appliance:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def operate(self):
        print(f"operating!")
        
    def info(self):
        print(f"brand: {self.brand}, model: {self.model}")

class WashingMachine(Appliance):
      def operate(self):
          print("Washing clothes!")
          
class Refrigerator(Appliance):
      def operate(self):
          print("Keeping foods cold")
          
class Microwave(Appliance):
      def operate(self):
          print("Heating food")
          
washingmachine = WashingMachine("LG", "wd40")
refrigerator = Refrigerator("condura", "f813")
microwave = Microwave("panasonic", "w734")


for appliance in [washingmachine, refrigerator, microwave]:
    appliance.operate()
    appliance.info()