
from weapon import Weapon

class Robot:

    def __init__(self, name):
        self.name = name
        self.attack_weapon = Weapon('Gunblade', 20)
        self.health = 100

    def attack(self, dinosaur):
        dinosaur.health -= self.attack_weapon.attack_power
        print(f'{self.name} strikes {dinosaur.name}!')
        print(f'{dinosaur.name} has {dinosaur.health} health points remaining.')
        print(" ")

 