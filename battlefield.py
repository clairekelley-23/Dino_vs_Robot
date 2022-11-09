# from weapon import Weapon
from dinosaur import Dinosaur
from robot import Robot


class Battlefield:

    def __init__(self):
       self.robot = Robot('Robo')
       self.dinosaur = Dinosaur('Fire Princess', 25)
    
    def run_game(self):
        self.display_welcome()
        print(" ")
        self.battle_phase()
        print(" ")
        self.display_winner()

    def display_welcome(self):
        print('\nWelcome to DINO vs ROBOT Domination!\nWho will be victorious!?')

    def battle_phase(self):
        while self.robot.health > 0 and self.dinosaur.health > 0:
            self.robot.attack(self.dinosaur)
            self.dinosaur.attack(self.robot)
        # pass

    def display_winner(self):
        if self.dinosaur == 0:
            print(f'{self.dinosaur.name} made {self.robot.name} extinct! Battle complete.')
        else:
            print(f'{self.robot.name} has defeated {self.dinosaur.name}. {self.dinosaur.name} is extinct.')
            