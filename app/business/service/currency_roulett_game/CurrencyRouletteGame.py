import logging

from app.business.service.AbstractGame import AbstractGame
import requests
import random


class CurrencyRouletteGame(AbstractGame):

    def get_money_interval(self, difficulty):
        random_num = random.randint(1, 101)
        print(f"Num is : {random_num}")
        url = f"https://api.apilayer.com/fixer/convert?to=ILS&from=USD&amount={random_num}"
        payload = {}
        headers = {
            "apikey": "dQkrYaLRbcxl5T3uKj8Pt4HZz5lm1bCz"
        }
        try:
            response = requests.request("GET", url, headers=headers, data=payload)
        except:
            logging.exception("Request was with exception")
            return 0, 0
        total_value_of_money = int(response.json()['result'])
        return total_value_of_money - (5 - difficulty), total_value_of_money + (5 - difficulty)

    def play(self, difficulty):
        interval = self.get_money_interval(difficulty)
        while True:
            try:
                input_from_user = int(input("Please, enter your number of money in ILS:\n"))
            except:
                print("Your input is not correct")
                continue
            if input_from_user < interval[0] or input_from_user > interval[1]:
                print("Range is from {} to {}". format(interval[0], interval[1]))
                print("Your input is {}".format(input_from_user))
                print("You lose!")
                break
            else:
                print("Range is from {} to {}".format(interval[0], interval[1]))
                print("Your input is {}".format(input_from_user))
                print("You win!")
                break
