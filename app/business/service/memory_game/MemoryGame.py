from app.business.service.AbstractGame import AbstractGame
import random
import sys
import time


class MemoryGame(AbstractGame):

    def generate_sequence(self, difficulty):
        return [random.randrange(1, 101, 1) for i in range(difficulty)]

    def get_list_from_user(self, difficulty):
        count = 0
        num_of_input = 1
        list_from_user = []
        is_finish = False
        while True:
            if is_finish or count == difficulty:
                break
            try:
                list_from_user.append(int(input(f"Enter value number {num_of_input}: ")))
                num_of_input += 1
                count += 1
            except:
                print("Your input is not correct")
            if is_finish or count == difficulty:
                break
            while True:
                input_finish_string = input(
                    "Do you want to finish input? If yes, please enter Y, if no, please enter N")
                if input_finish_string.lower() == 'y':
                    is_finish = True
                    break
                elif input_finish_string.lower() == 'n':
                    break
                else:
                    continue

        return list_from_user

    def is_list_equal(self, random_sequence, list_from_user):
        random_sequence.sort()
        list_from_user.sort()
        return random_sequence == list_from_user

    def play(self, difficulty):
        random_sequence = self.generate_sequence(difficulty)
        print("You have 3 seconds to remember these numbers!")
        sys.stdout.write(str(random_sequence))
        time.sleep(3)
        sys.stdout.write("\r")
        list_from_user = self.get_list_from_user(difficulty)
        if self.is_list_equal(random_sequence, list_from_user):
            print("You win!")
        else:
            print(f"values of computer is {random_sequence}")
            print(f"your values is {list_from_user}")
            print("You lose!")

    def game_continue(self):
        try:
            input("Do you want to finish input? If yes, please enter Y, if no, please "
                  "enter N")
        except:
            print("Your input is not correct")

