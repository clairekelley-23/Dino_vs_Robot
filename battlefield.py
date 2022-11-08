# from weapon import Weapon
from dinosaur import Dinosaur
from robot import Robot


class Battlefield:

    def __init__(self):
       self.robot = Robot('Lord Pipes')
       self.dinosaur = Dinosaur('Gus', 25)
    
    def run_game(self):
        self.display_welcome()
        self.battle_phase()
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
            print(f'{self.dinosaur} made {self.robot} extinct! Battle complete.')
        else:
            print(f'{self.robot} has defeated {self.dinosaur}. {self.dinosaur} is extinct.')
            