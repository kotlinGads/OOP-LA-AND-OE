print("LA15")

class Dog:
    def __init__(self,name):
        self.name = name
    def speak(self):
        print(f"{self.name} says: aww aww")
        
class Cat:
    def __init__(self,name):
        self.name = name
    def speak(self):
        print(f"{self.name} says: meow moew")
        
        
class Bird:
    def __init__(self,name):
        self.name = name
    def speak(self):
        print(f"{self.name} says: womp womp")
        
        
class fish:
    def __init__(self,name):
        self.name = name
    def speak(self):
        print(f"{self.name} says: wala")   
        
dog = Dog("doggy")      
cat = Cat("moewwy") 
bird = Bird("birdy")   
fish = fish("fish")      
        
def animal_sound(animal):
    print(animal.speak())
    
animal_sound(dog)
animal_sound(cat)
animal_sound(bird)
animal_sound(fish)        
                

for animal in [dog, cat, bird, fish]:
    print(animal.speak())
            