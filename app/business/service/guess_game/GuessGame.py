from app.business.service.AbstractGame import AbstractGame
import random
import logging


class GuessGame(AbstractGame):

    def generate_number(self, difficulty):
        return random.randint(1, difficulty + 1)

    def get_guess_from_user(self, difficulty):
        while True:
            print(f"Please enter number from 1 to {difficulty}")
            try:
                input_res = int(input())
                if input_res < 1 or input_res > difficulty:
                    continue
                else:
                    break
            except:
                logging.info("Your input is not digit")
        return input_res

    def play(self, difficulty):
        gen_num = self.generate_number(difficulty)
        get_guess_from_user = self.get_guess_from_user(difficulty)
        if gen_num == get_guess_from_user:
            print("You win!")
        else:
            print("You lose!")
