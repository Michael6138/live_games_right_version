from app.business.service.currency_roulett_game.CurrencyRouletteGame import CurrencyRouletteGame
from app.business.service.guess_game.GuessGame import GuessGame
from app.business.service.memory_game.MemoryGame import MemoryGame


def welcome(name):
    return "Hello {} and welcome to the World of Games (WoG).Here you can find many cool games to play.".format(name)


def load_text():
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")


def load_text_difficulty():
    print("Please choose game difficulty from 1 to 5:")


def load_game():
    while True:
        try:
            load_text()
            game = int(input())
            if game > 3 or game < 1:
                load_text()
            else:
                break
        except:
            print("Your input is not correct")
    load_text_difficulty()
    while True:
        try:
            difficulty = int(input())
            if difficulty > 5 or difficulty < 1:
                load_text_difficulty()
            else:
                break
        except:
            print("Your input is not correct, input number from 1 to 5")
    if game == 1:
        MemoryGame().play(difficulty)
    elif game == 2:
        GuessGame().play(difficulty)
    elif game == 3:
        CurrencyRouletteGame().play(difficulty)

