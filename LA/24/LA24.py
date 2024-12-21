print("LA #24")

from abc import ABC, abstractmethod

class GameCharacter(ABC):
    def __init__(self, name):
        self.name = name 
    
    @abstractmethod
    def attack(self):
        pass
    

class Warrior(GameCharacter):
    def attack(self):
        print("Swings Sword!")      
        
class Mage(GameCharacter):
    def attack(self):
        print("Casts a fireball!")   
        
class Archer(GameCharacter):
    def attack(self):
        print("Shoots an arrow!")   
        
class Healer(GameCharacter):
    def attack(self):
        print("Cast healing spell on ally!")
                                   
        
ch1 = Warrior("Daniel")
ch2 = Mage("Aron")
ch3 = Archer("Johnree")
ch4 = Healer("Arnaldo")

ch1.attack()
ch2.attack()
ch3.attack()
ch4.attack()