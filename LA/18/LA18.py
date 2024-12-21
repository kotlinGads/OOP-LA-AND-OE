print("LA # 18")

class Sinigang:
    def __init__(self, meat, tomato, onion, fish_sauce, vegetable, tamarind):
        self.meat = meat
        self.tomato = tomato
        self.onion = onion
        self.fish_sauce = fish_sauce
        self.vegetable = vegetable
        self.tamarind = tamarind

    def __str__(self):
        return f"Ang paborito kong sinigang ay may {self.meat}, {self.tomato}, {self.onion}, {self.fish_sauce}, {self.vegetable}, {self.tamarind}"

sigang1 = Sinigang("Baboy", "1 tomato", "1 red onion", "fish sauce", "radish", "tamarind")
sigang2 = Sinigang("Manok", "2 tomato", "2 red onion", "fish sauce", "kangkong", "tamarind")
sigang3 = Sinigang("Manok at Baboy", "3 tomato", "3 red onion", "fish sauce", "radish at kangkong", "tamarind")

print(sigang1)
print(sigang2)
print(sigang3)