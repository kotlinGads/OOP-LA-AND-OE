print("LA 25")

from abc import ABC, abstractmethod

class Character(ABC):
    @property
    @abstractmethod    
    def alias(self):
        pass
    
class Batman(Character):
    def __init__(self, real_name, alias):
        
        self.real_name = real_name
        self.__alias = alias
        
    @property 
    def alias (self):
        return self.__alias
    
Paniki = Batman("Bruce Wayne", "Batman")
print(Paniki.alias)