
# Soldier


import random


class Soldier():
   
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
            return self.strength
        
    def receiveDamage(self, damage):
            self.health -= damage
       







# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength) 
        self.name = name
        
    def receiveDamage(self, damage):
        
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
        
    def battleCry(self):
        return "Odin Owns You All!"






# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    
    def receiveDamage(self, damage):
        
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

# War


class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    
    def addViking(self, viking):
        self.vikingArmy.append(viking)
        

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    
    def vikingAttack(self):
        random_viking = random.choice(self.vikingArmy)
        random_saxon = random.choice(self.saxonArmy)

        damage = random_saxon.receiveDamage(random_viking.strength)

        if random_saxon.health <= 0:
            self.saxonArmy.remove(random_saxon)
        return damage
        
        
    def saxonAttack(self):
        random_viking = random.choice(self.vikingArmy)
        random_saxon = random.choice(self.saxonArmy)

        damage = random_viking.receiveDamage(random_saxon.strength)
        
        if random_viking.health <= 0:
            self.vikingArmy.remove(random_viking)
        return damage
    
    
    def showStatus(self):
        
        if self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
             

        elif self.saxonArmy == []:
            return "Vikings have won the war of the century!"
        
        else:
            return "Vikings and Saxons are still in the thick of battle."
