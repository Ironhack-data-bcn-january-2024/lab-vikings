
# Soldier
import random
class Soldier:
    def __init__ (self, health, strength):
        self.health = health
        self.strength = strength
    def attack (self):
        return self.strength
    def receiveDamage (self, damage):
        self.health -= damage
class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.health = health
        self.strength = strength
        self.name = name
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    def battleCry(self):
        return f"Odin Owns You All!"
class Saxon(Soldier):
    def __init__ (self, health, strength):
        self.health = health
        self.strength = strength
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"
        
class War():
    def __init__ (self):
        self.vikingArmy = []
        self.saxonArmy= []
    def addViking(self, viking):
        self.vikingArmy.append(viking)
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    def vikingAttack(self):
        saxon_army = random.choice(self.saxonArmy)
        viking_army = random.choice(self.vikingArmy)
        damage_to_saxon = saxon_army.receiveDamage(viking_army.strength)   
        if saxon_army.health <= 0:
            self.saxonArmy.remove(saxon_army) 
        return damage_to_saxon
    def saxonAttack(self):
        viking_army = random.choice(self.vikingArmy)
        damage_to_viking = viking_army.receiveDamage(viking_army.strength)
        if viking_army.health <= 0:
            self.vikingArmy.remove(viking_army)
        return damage_to_viking
   
    def showStatus(self):
      if len(self.vikingArmy) == 0:
          return "Vikings have won the war of the century!"
      elif len(self.saxonArmy) == 0:
          return "Saxons have fought for their lives and survive another day..."
      else:
          return "Vikings and Saxons are still in the thick of battle."
      
      
      """
# Viking
class Viking(Soldier):
    def __int__ (self, name, health, strength):
        self.name = name
        self.health = health
                self.strength = strength       
    def receiveDamageViking(self, the_damage):
        self.health -= the_damage       
        if the_damage > 0:
                    return f"{self.name} has received {the_damage} points of damage"            
        if the_damage < self.health:
            return f"{self.name} has died in act of combat"
    def battleCry(self):
        return "Odin owns You All!"
"""   