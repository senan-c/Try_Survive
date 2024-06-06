import random


class Boss:
    def __init__(self, name):
        self.name = name
        self.health = 200
        
        if self.name == "Infected Commander":
            self.health += 300
            
        if self.name == "Diseased Doctor":
            self.health += 50
            
        if self.name == "Fuel Beast":
            self.health += 100
            
    def attack(self):
        chance = random.randint(1,3)
        if self.name == "Infected Commander":          
            if chance == 1:
                print("The", self.name,"hits you with its breaching hammer")
                
            elif chance == 2:
                print("The", self.name,"swings and crushes you with its breaching hammer")
                
            else:
                print("You try dodge but the", self.name,"catches you with a pulverising blow")
                
        elif self.name == "Diseased Doctor":    
            if chance == 1:
                print("The", self.name,"slices you with its scalpel")
                
            elif chance == 2:
                print("The", self.name,"jumps and cuts you with its scalpel")
                
            elif chance == 3:
                print("The", self.name,"leaps at you and carves you with its scalpel")
                
        elif self.name == "Fuel Beast":
            if chance == 1:
                print("The", self.name,"delivers a scorching blow")
                
            elif chance == 2:
                print("The", self.name,"slashes at you, burning your flesh")
                
            elif chance == 2:
                print("The", self.name,"attacks you with a flaming chop of its hand-axe")
                
    def miss(self):
        chance = random.randint(1,3)
        if chance == 1:
            print("The", self.name, "swings at your head, but you duck and it misses")
            
        elif chance == 2:
            print("The", self.name, "swipes at your neck but you dodge just in time")
        
        else:
            print("You dodge and manage to evade the ", self.name + "'s", "swing")
            
    def dodge(self):
        chance = random.randint(1, 3)
        if chance == 1:
            print("The", self.name, "dodges your attack")
            
        elif chance == 2:
            print("The", self.name, "blocks your attack easily")
            
        elif chance == 3:
            print("The", self.name, "barely blocks your attack, but is unfazed")
            
    def shout(self):
        chance = random.randint(1, 4)
        if self.name == "Infected Commander":
            if chance == 1:
                print("The", self.name, "roars and pounds its chest")
            
            elif chance == 2:
                print("The", self.name, "looks at you and bellows")
            
            elif chance == 3:
                print("It thrashes its head from side to side and roars")
                
            else:
                print("The", self.name, "swings its hammer from side to side and shakes the room")
                
        elif self.name == "Diseased Doctor":
            if chance == 1:
                print("The", self.name, "screeches and glares at you")
            
            elif chance == 2:
                print("The", self.name, "howls and scratches at the ground")
            
            elif chance == 3:
                print("It stabs at the air with its scalpel")
                
            else:
                print("The", self.name, "spits at you and howls")
                
        elif self.name == "Fuel Beast":
            if chance == 1:
                print("The", self.name, "roars as flame drips from its body")
                
            elif chance == 2:
                print("The", self.name, "slashes at the air with its superheated axe")
            
            elif chance == 3:
                print("The", self.name, "glares at you as it flesh bubbles beneath the suit")
                
            else:
                print("The", self.name, "charges at you, leaving burning footprints in its wake")