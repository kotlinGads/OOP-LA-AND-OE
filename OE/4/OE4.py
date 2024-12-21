class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, target):
        target.health -= self.power
        print(f"{self.name} attacks {target.name}! {target.name}'s remaining health: {target.health}")

    def special_move(self):
        pass

    def defend(self, attacker):
        self.health -= attacker.power


class Warrior(Character):
    def special_move(self):
        print(f"{self.name} uses Shield Bash! Doubling attack power for the next attack.")
        self.power *= 2


class Mage(Character):
    def special_move(self):
        print(f"{self.name} casts Fireball! Reducing target's health by 100 points.")
        self.attack(self)


class Archer(Character):
    def special_move(self):
        print(f"{self.name} shoots a Piercing Arrow! Ignoring target's defense.")
        self.power *= 1.5


class Monster(Character):
    def special_move(self):
        print(f"{self.name} roars and gains extra health!")
        self.health += 50

warrior = Warrior("Warrior", 150, 20)
mage = Mage("Mage", 120, 15)
archer = Archer("Archer", 100, 25)
monster = Monster("Monster", 200, 30)

characters = [warrior, mage, archer]

for character in characters:
    character.attack(monster)
    monster.special_move()
    if monster.health <=0:
        print("Monster has been defeated!")
        break
    monster.attack(character)
    character.defend(monster)
    if character.health <=0:
        print(f"{character.name} has been defeated!")

for character in characters + [monster]:
    character.special_move()