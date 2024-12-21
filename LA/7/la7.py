print("LA #7")
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
carbrand = Car("Toyota", "Red")
carbrand2 = Car("Honda", "Black")
print(f"{carbrand.brand}, {carbrand.color}")
carbrand.color = "Gray"
print(f"{carbrand.brand}, {carbrand.color}")
print(f"{carbrand2.brand}, {carbrand2.color}")