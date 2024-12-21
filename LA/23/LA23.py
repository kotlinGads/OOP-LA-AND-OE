print("LA #23")

class AnimeCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability
    
    def introduce(self, func):
        def wrapper(*args, **kwargs):
            print("Introducing...")
            func(*args, **kwargs)
            print("This character is amazing!")
        return wrapper

Char = AnimeCharacter("Vegeta", "Final Flash")

@Char.introduce
def character_info():
    print(f"I am {Char.name} and I can use {Char.ability}")

character_info()