from weapon import Weapon

class Robot:

    def __init__(self, name):
        self.name = name
        self.attack_weapon = Weapon('Gunblade', 20)
        self.heath = 100

    def attack(self, dinosaur):
        dinosaur.health -= self.attack_weapon.attack_power

    # def user_input(self):
    #     weapon_name = input("What is the name of your weapon? ")
    #     weapon_attack = int(input("What is the attack power of your weapon? "))
    #     self.attack_weapon = Weapon(weapon_name, weapon_attack)