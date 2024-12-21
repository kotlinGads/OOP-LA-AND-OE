print("LA #10")

class Vehicle:
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type

    def describeVehicle(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Fuel Type: {self.fuel_type}")

class Car(Vehicle):
    pass

class Motorcycle(Vehicle):
    pass

my_car = Car("Toyota", "Vios", "Gasoline")
my_motorcycle = Motorcycle("Suzuki", "Raider", "Gasoline")

my_car.describeVehicle()
my_motorcycle.describeVehicle()