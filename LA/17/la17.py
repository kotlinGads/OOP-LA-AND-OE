class Player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    def attack(self, target):
        target.health = target.health - self.attack_power
        print(f"{self.name} attack {target.name} for {self.attack_power} damage")
        print(f"{target.name} remaining heatlh {target.health}\n")
player1 = Player("Aeron", 100, 20)
player2 = Player("Daniel", 80, 10)
player1.attack(player2)
while player1.health > 0 and player2.health > 0:
    player1.attack(player2)
    if player2.health <= 0:
        print(f"{player1.name} wins")
        break
    player2.attack(player1)
    if player1.health <= 0:
        print(f"{player2.name} wins")
        break