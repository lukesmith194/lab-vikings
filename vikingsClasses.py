import random

# Soldier


class Soldier:
    def __init__ (self,health, strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - damage



# Viking


class Viking(Soldier):
    def __init__ (self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
    def receiveDamage(self, damage):
        self.damage = damage
        self.health= self.health - damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    def battleCry(self):
        return ("Odin Owns You All!")
# Saxon


class Saxon(Soldier):
    def __init__ (self, health, strength):
        super().__init__(health, strength)
    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health <= 0:
            return f"A Saxon has died in combat"
        else:
            return f"A Saxon has received {damage} points of damage"




# War


class War():

    def __init__ (self):
        self.vikingArmy =[]
        self.saxonArmy =[]

    
    def addViking(self,Viking):
        self.vikingArmy.append(Viking)

    
    def addSaxon(self,Saxon):
        self.saxonArmy.append(Saxon)

    
    def vikingAttack(self):
        V = random.choice(self.vikingArmy)
        S = random.choice(self.saxonArmy)
        
        S.receiveDamage(V.strength)
        if S.health <= 0:
            self.saxonArmy.remove(S)
            return "A Saxon has died in combat"
        else:
            return f"Saxon has received {V.strength}"
    
    def saxonAttack(self):
        V = random.choice(self.vikingArmy)
        S = random.choice(self.saxonArmy)

        V.receiveDamage(S.strength)
        if V.health <= 0:
            self.vikingArmy.remove(V)
            return "Viking has died in combat"
        else:
            return f"{V.name} has received {S.strength} points of damage"


    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."