class Enemy:

    def __init__(self,name,classtype,health,mana):
        self.name = name
        self.classtype = classtype
        self.health = health
        self.mana = mana

    def info(self):
        print(f"I am {self.name} the {self.classtype} I have {self.health}HP")

Warrior = Enemy("Timmy","Warrior",150,10)
Warrior.info()