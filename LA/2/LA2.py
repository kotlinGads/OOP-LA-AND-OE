print("LA #2")
class character():
    def __init__(self,name,type, damage_type):
        self.name = name
        self.type = type
        self.damage_type = damage_type

hero = character("Clint", "Marksman", "Physical Damage")
hero2 = character("Terizla", "Fighter", "Physical Damage")


print(hero.name, hero.type, hero.damage_type , hero2.name, hero2.type, hero2.damage_type)