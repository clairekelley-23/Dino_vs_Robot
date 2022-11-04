from weapon import Weapon
from dinosaur import Dinosaur
from robot import Robot


class Battlefield:

    def __init__(self):
       Robot.name = "Lord Pipes"
       Dinosaur.name = "Gus"
    
    def run_game(self):
        game = self.display_welcome
        game = self.battle_phase
        game = self.display_winner
        print(game)

        return 
        # game = self.display_welcome, self.battle_phase
        # welcome = print(self.display_welcome)


    def display_welcome(self):
        print('\nWelcome to DINO vs ROBOT Domination!\nWho will be victorious!?')

    def battle_phase(self):
        Robot.attack = self.dinosaur.attack.health
        print('Lord Pipes strikes Gus!')
        Dinosaur.attack = self.robot.attack.health
        print('Gus has damaged Lord Pipes!')
        
        # pass

    def display_winner(self):
        if Dinosaur == 0:
            print("Lord Pipes has won the battle! Gus is extinct.")