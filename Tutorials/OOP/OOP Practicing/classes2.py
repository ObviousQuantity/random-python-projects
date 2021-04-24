class Enemy:
    number_of_enemies = 0

    def __init__(self,name,classtype,health,mana):
        self.name = name
        self.classtype = classtype
        self.health = health
        self.mana = mana
        self.guild = False
        Enemy.add_enemy()
    
    def info(self):
        print(f"I am {self.name} the {self.classtype} I have {self.health}HP and {self.mana}MP")

    def in_guild(self):
        if self.guild == True:
            print("IS IN GUILD")
        else:
            print("NOT IN GUILD")

    @classmethod
    def get_total_enemies(cls):
        return cls.number_of_enemies

    @classmethod
    def add_enemy(cls):
        cls.number_of_enemies += 1

class Guild:
    def __init__(self,guild_name,max_members):
        self.guild_name = guild_name
        self.max_members = max_members
        self.members = []

    def join_guild(self,name):
        if len(self.members) < self.max_members:
            self.members.append(name)
            name.guild = True
            print(f"{name.name} has joined the guild!")

    def leave_guild(self,name):
        self.members.remove(name)
        name.guild = False
        print(f"{name.name} has left the guild!")

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

Wizard1 = Wizard("Pepe","Mage",90,200,50)
Wizard2= Wizard("Frosty","Mage",75,300,50)

Warrior1 = Warrior("Asmongold","Warrior",100,30,0)
Warrior2 = Warrior("Dominic","Warrior",100,30,0)
Warrior3 = Warrior("Billy","Warrior",100,30,0)

Guild = Guild("Savage Inc",3) #Guild Name: Savage Inc | Max Members: 3
Warrior1.in_guild()
Guild.join_guild(Warrior1)
Warrior1.in_guild()
Guild.leave_guild(Warrior1)
Warrior1.in_guild()

print("There are "+str(Enemy.get_total_enemies())+" amount of enemies!")
print(str(Wizard.get_total_wizards())+" of them are wizards!")
print(str(Warrior.get_total_warriors())+" of them are warriors!")