print ("LA #13")

class Animal():
    def __init__(self,name,type):
         self.name = name
         self.type = type
    
    def describeFish(self):
        print(f'{self.name},{self.type}')
        
class Fish(Animal):         
    def __init__(self,name,type, can_swim):
        super().__init__(name,type)
        self.can_swim = can_swim
    
tilapya = Fish("Tilapya", "Fish", True or False)
print(tilapya.can_swim) 