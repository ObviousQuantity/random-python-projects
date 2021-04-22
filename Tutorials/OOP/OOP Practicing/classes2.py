class Enemy:
    def __init__(self,name,classtype,health,mana):
        self.name = name
        self.classtype = classtype
        self.health = health
        self.mana = mana
    
    def info(self):
        print(f"I am {self.name} the {self.classtype} I have {self.health}HP and {self.mana}MP")

class Wizard(Enemy):
    def __init__(self,name,classtype,health,mana,magicdefense):
        super().__init__(name,classtype,health,mana) 
        self.magicdefense = magicdefense

    def fireblast(self):
        print("POGGERS EPIC FIRE BLAST")

w = Wizard("Pepe","Mage",90,200,50)
w.info()
w.fireblast()

class Warrior(Enemy):
    def __init__(self,name,classtype,health,mana,defense):
        super().__init__(name,classtype,health,mana)
        self.defense = defense 

    def strike(self):
        print("Lame sword attack")

w = Wizard("Pepe","Mage",90,200,50)
w.info()
w.fireblast()
