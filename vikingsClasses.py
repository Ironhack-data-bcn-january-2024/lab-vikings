
import random

class Soldier ():
    
    def __init__ (self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage



class Viking(Soldier):

    def __init__ (self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def receiveDamage(self, damage):
        self.health -= damage
        if  self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        else:
            return f'{self.name} has died in act of combat'

    def battleCry(self):
        return "Odin Owns You All!"


class Saxon(Soldier):

    def __init__ (self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health -= damage
        if  self.health > 0:
            return f'A Saxon has received {damage} points of damage'
        else:
            return f'A Saxon has died in combat'



class War():


    def __init__ (self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.viking = viking
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxon = saxon
        self.saxonArmy.append(saxon)

    def vikingAttack(self):

        v_i = random.randint(0,len(self.vikingArmy)-1)
        random_viking = self.vikingArmy[v_i]

        s_i = random.randint(0,len(self.saxonArmy)-1)
        random_saxon = self.saxonArmy[s_i]

        #valida que daño asociado asi  te valga 
        daño = random_saxon.receiveDamage(random_viking.strength)
        if random_saxon.health <= 0:
            self.saxonArmy.remove(random_saxon)
        return daño

    def saxonAttack(self):

        v_i = random.randint(0,len(self.vikingArmy)-1)
        random_viking = self.vikingArmy[v_i]

        s_i = random.randint(0,len(self.saxonArmy)-1)
        random_saxon = self.saxonArmy[s_i]

        daño = random_viking.receiveDamage(random_saxon.strength)
        if random_viking.health <= 0:
            self.vikingArmy.remove(random_viking)
        return daño

    def showStatus(self):
        
        if self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        elif self.saxonArmy == []:
            return "Vikings have won the war of the century!"
        else:
            return "Vikings and Saxons are still in the thick of battle."
