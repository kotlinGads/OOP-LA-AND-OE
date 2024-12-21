print("LA #9")
class Car:
    def __init__(self, brand):
        self.brand = brand
    def __str__(self):
        return self.brand
kotse = Car("Toyota")
print(kotse.brand)
del kotse
print(kotse)