class BirthdayParty:
    def __init__(self, theme, foods, special_dish):
        self.theme = theme
        self.foods = foods
        self.special_dish = special_dish
    
    def __secret_dish(self):
        print("Secret Dish: Buko Salad")
    
    def show_foods(self):
        print(f"Theme: {self.theme}")
        print("Food list:")
        for food in self.foods:
            print(f"- {food}")
        print(f"Special Dish: {self.special_dish}")
        self.__secret_dish() 

party1 = BirthdayParty("1st Birthday", ["bbq", "chicken curry", "menudo"], "lechon")
party2 = BirthdayParty("7th Birhtday", ["menudo", "lechon", "chicken pastel"], "hotdog")
party3 = BirthdayParty("Debut", ["Pansit", "spaghetti", "palabok"], "Adobong aso")

party1.show_foods()
print("\n")
party2.show_foods()
print("\n")
party3.show_foods()