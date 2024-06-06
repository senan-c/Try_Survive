import random


class Human: 
    def __init__(self, name, weapon, armour):
        self.name = name
        self.health = 100
        self.weapon = weapon
        self.armour = armour
        
        if self.armour is not None:
            if self.armour == "(clothing) *army helmet*":
                self.health += 30
                
            elif self.armour == "(clothing) *body armour*":
                self.health += 75
                
            elif self.armour == "(clothing) *leather jacket*":
                self.health += 15
            
            elif self.armour == "(clothing) *motorbike helmet*":
                self.health += 20
                
            elif self.armour == "(clothing) *police vest*":
                self.health += 40
                
            elif self.armour == "(clothing) *combat pants*" or self.armour == "(clothing) *work boots*":
                self.health += 10
                
            elif self.armour == "(clothing) *leather gloves*":
                self.health += 5
                
    def display_armour(self):
        if self.armour is not None:
            print("It looks like", self.name,"is wearing", self.armour)
        
        else:
            print("It looks like", self.name,"is unarmoured")
    
    def attack(self):
        chance = random.randint(1, 2)
        if self.weapon[9:] == "machete" or self.weapon[9:] == "knife":
            if chance == 1:
                print("He stabs you with his", self.weapon[9:])

            else:
                print(self.name, "slashes you with his", self.weapon[9:])
            
        elif self.weapon == "hands":
            if chance == 1:
                print("He swings and punches you in the head")

            else:
                print(self.name, "kicks you as hard as he can")
                
        else:
            if chance == 1:
                print("He whacks you with his", self.weapon[9:])

            else:
                print(self.name, "clubs you with his", self.weapon[9:])
                
    def miss(self):
        chance = random.randint(1,3)
        if chance == 1:
            print(self.name, "swings at your head, but you duck and he misses")
            
        elif chance == 2:
            print(self.name, "swipes at your neck but you dodge just in time")
        
        else:
            print("You dodge and manage to evade", self.name + "'s", "swing")
                
    def dodge(self):
        chance = random.randint(1, 3)
        if chance == 1:
            print(self.name, "dodges your attack")
            
        elif chance == 2:
            print("He ducks under your strike")
            
        elif chance == 3:
            print(self.name, "barely dodges your attack")