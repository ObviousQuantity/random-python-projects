class Enemy:
    number_of_enemies = 0

    def __init__(self,name,classtype,health,mana):
        self.name = name
        self.classtype = classtype
        self.health = health
        self.mana = mana
        Enemy.add_enemy()
    
    def info(self):
        print(f"I am {self.name} the {self.classtype} I have {self.health}HP and {self.mana}MP")

    @classmethod
    def get_total_enemies(cls):
        return cls.number_of_enemies

    @classmethod
    def add_enemy(cls):
        cls.number_of_enemies += 1

class Wizard(Enemy):
    number_of_wizards = 0

    def __init__(self,name,classtype,health,mana,magicdefense):
        super().__init__(name,classtype,health,mana) 
        self.magicdefense = magicdefense
        Wizard.add_wizard()

    def fireblast(self):
        print("POGGERS EPIC FIRE BLAST")

    @classmethod
    def get_total_wizards(cls):
        return cls.number_of_wizards

    @classmethod
    def add_wizard(cls):
        cls.number_of_wizards += 1   

class Warrior(Enemy):
    number_of_warriors = 0

    def __init__(self,name,classtype,health,mana,defense):
        super().__init__(name,classtype,health,mana)
        self.defense = defense 
        Warrior.add_warrior()

    def strike(self):
        print("Lame sword attack")

    @classmethod
    def get_total_warriors(cls):
        return cls.number_of_warriors

    @classmethod
    def add_warrior(cls):
        cls.number_of_warriors += 1   

w = Wizard("Pepe","Mage",90,200,50)
w2 = Wizard("Frosty","Mage",75,300,50)
w3 = Warrior("Asmongold","Warrior",100,30,0)
#w2.info()
#w2.fireblast()
print("There are "+str(Enemy.get_total_enemies())+" amount of enemies!")
print(str(Wizard.get_total_wizards())+" of them are wizards!")
print(str(Warrior.get_total_warriors())+" of them are warriors!")
