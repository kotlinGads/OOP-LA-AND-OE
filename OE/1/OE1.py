class hero():
    def __init__(self, name, role, dmg_type, health, auto_atk_dmg):
        self.name = name
        self.role = role
        self.dmg_type = dmg_type
        self.health = health
        self.auto_atk_dmg = auto_atk_dmg
    def describe(self):
        return f"{self.name} is a {self.role} with a {self.dmg_type} power"
    
hero_mm1 = hero("Brody", "marksman", "Physical attack", 2290, 105)
hero_fighter1 = hero ("Terizla", "fighter", "physical attack", 2728, 129)
hero_support1 = hero("Mathilda", "support", "magic damage", 2651, 120)
hero_mage1 = hero("lunox", "mage", "magic damage", 2621, 115)
hero_jungler = hero("Ling", "Assasin", "attack damage", 2528, 125)

print(f'''
      {hero_mm1.name}
      {hero_mm1.role}
      {hero_mm1.health} HP
      {hero_mm1.auto_atk_dmg} auto attack
      {hero_mm1.dmg_type}
      {hero_mm1.describe()}

      {hero_fighter1.name}
      {hero_fighter1.role}
      {hero_fighter1.health} HP
      {hero_fighter1.auto_atk_dmg} auto attack
      {hero_fighter1.dmg_type}
      {hero_fighter1.describe()}

      {hero_support1.name}
      {hero_support1.role}
      {hero_support1.health} HP
      {hero_support1.auto_atk_dmg} auto attack
      {hero_support1.dmg_type}
      {hero_support1.describe()}
      
      {hero_mage1.name}
      {hero_mage1.role}
      {hero_mage1.health} HP
      {hero_mage1.auto_atk_dmg} auto attack
      {hero_mage1.dmg_type}
      {hero_mage1.describe()}
      
      {hero_jungler.name}
      {hero_jungler.role}
      {hero_jungler.health} HP
      {hero_jungler.auto_atk_dmg} auto attack
      {hero_jungler.dmg_type}
      {hero_jungler.describe()}
      ''')