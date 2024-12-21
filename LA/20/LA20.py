class Sinigang:
    def __init__(self, meat, tomato, onion, fish_sauce, vegetable, tamarind, sili):
        self.meat = meat
        self.tomato = tomato
        self.onion = onion
        self.fish_sauce = fish_sauce
        self.vegetable = vegetable
        self.tamarind = tamarind
        self.__sili = sili

    def __str__(self):
        return f"Ang paborito kong sinigang ay may {self.meat}, {self.tomato}, {self.onion}, {self.fish_sauce}, {self.vegetable}, {self.tamarind}"
    def may_sili(self):
        return self.__sili
sigang1 = Sinigang("Baboy", "1 tomato", "1 red onion", "fish sauce", "radish", "tamarind", "3 siling green")
print(sigang1.may_sili())
